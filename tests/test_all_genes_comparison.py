"""Pure parsing/statistics checks. Never run a predictor or load the real dataset."""
from array import array
import gzip
import math

import pytest

from validation.controls_2010.compare_all_genes import (
    Moments, correlation_stats, map_measurements, read_annotation,
    read_fasta, read_wig, summarize_models, validate_mapping, window_records,
)


def compressed(tmp_path, name, text):
    path = tmp_path/name
    with gzip.open(path,'wt') as stream:
        stream.write(text)
    return path


def test_correlations_handle_ties_and_constant_or_insufficient_data():
    stats = correlation_stats([1,1,2,3],[1,2,3,4],3)
    assert stats['spearman'] == pytest.approx(math.sqrt(.9))
    assert correlation_stats([1,2,3],[3,2,1],3)['pearson'] == pytest.approx(-1)
    assert correlation_stats([1,1,1],[2,3,4],3)['pearson'] is None
    assert correlation_stats([1,1,1],[2,3,4],3)['spearman'] is None
    insufficient = correlation_stats([1,2],[2,3],3)
    assert insufficient['pearson'] is None and insufficient['n_pairs']==2
    with pytest.raises(ValueError,match='Unmatched'):
        correlation_stats([1],[1,2],3)


def test_pooled_moments_merge_matches_direct_computation():
    first = correlation_stats([1,2,3],[2,5,4],3)
    second = correlation_stats([4,5,6],[8,7,10],3)
    pooled = Moments(first['moments'])
    pooled.merge(Moments(second['moments']))
    direct = correlation_stats([1,2,3,4,5,6],[2,5,4,8,7,10],3)
    assert pooled.correlation()==pytest.approx(direct['pearson'])
    summary = summarize_models({'example':[first,second]},3)['example']
    assert summary['n_pairs']==6
    assert summary['pooled_pearson']==pytest.approx(direct['pearson'])
    assert summary['median_gene_pearson']==pytest.approx((first['pearson']+second['pearson'])/2)


def test_mapping_preserves_zero_missingness_and_reverse_coordinates():
    wig = ({'chrI':array('I',[10,11,13,14])},
           {'chrI':array('d',[0.,2.,-3.,4.])})
    forward,ambiguous = map_measurements(('1',10,14),wig)
    assert forward=={1:0.,2:2.,4:-3.,5:4.} and ambiguous==0
    reverse,_ = map_measurements(('1',14,10),wig)
    assert reverse=={5:0.,4:2.,2:-3.,1:4.}
    excluded,n = map_measurements(('1',14,10),wig,[(11,13)])
    assert excluded=={5:0.,1:4.} and n==2
    retained,n = map_measurements(('1',14,10),wig,[(11,13)],False)
    assert retained==reverse and n==2


def test_genomic_reconstruction_requires_exact_sequence():
    genome = {'1':'AACGTCAA'}
    validate_mapping('CGUC',('1',3,6),genome)
    validate_mapping('GACG',('1',6,3),genome)
    with pytest.raises(ValueError,match='cannot be reconstructed'):
        validate_mapping('AAAA',('1',3,6),genome)


def test_spliced_projection_uses_only_exact_annotated_blocks():
    genome = {'1':'AACGTCAA'}
    blocks = [('1',3,3),('1',5,6)]
    assert validate_mapping('CUC',('1',3,6),genome,blocks)==(3,5,6)
    assert validate_mapping('GAG',('1',6,3),genome,blocks)==(6,5,3)
    wig = ({'chrI':array('I',[3,4,5,6])},{'chrI':array('d',[.5,0.,-.2,.1])})
    pars,ambiguous = map_measurements(('1',3,6),wig,[(4,4)],True,(3,5,6))
    assert pars=={1:.5,2:-.2,3:.1} and ambiguous==0
    with pytest.raises(ValueError,match='cannot be reconstructed'):
        validate_mapping('AAA',('1',3,6),genome,blocks)


def test_input_readers_refuse_duplicate_records_and_coordinates(tmp_path):
    path = compressed(tmp_path,'sequences.gz','>gene\nac\ngt\n')
    assert read_fasta(path)=={'gene':'ACGT'}
    path = compressed(tmp_path,'duplicate.gz','>gene\nAC\n>gene\nGU\n')
    with pytest.raises(ValueError,match='Duplicate FASTA'):
        read_fasta(path)
    path = compressed(tmp_path,'annotation.gz','gene\t1\t10\t14\tTranscript\n')
    assert read_annotation(path)=={'gene':('1',10,14)}
    path = compressed(tmp_path,'scores.gz','track name="PARS"\nvariableStep chrom=chrI\n10 0\n14 -2\n')
    positions,values = read_wig(path)
    assert list(positions['chrI'])==[10,14] and list(values['chrI'])==[0.,-2.]
    path = compressed(tmp_path,'duplicate_scores.gz','variableStep chrom=chrI\n10 0\n10 2\n')
    with pytest.raises(ValueError,match='Duplicate/out-of-order'):
        read_wig(path)


def test_window_seed_is_best_segment_not_union_and_requires_all_placements():
    # This is a precomputed table; this test invokes no folding calculation.
    table = {1:[None,1.],2:[None,1.,.2],3:[None,1.,.7],4:[None,1.,.5,None,.05]}
    pars = {1:0.,2:1.,3:2.,4:3.}
    rows = list(window_records('ACGU',pars,table,4,2,1,1.))
    assert len(rows)==1
    assert rows[0]['full_p']==.05 and rows[0]['seed_p']==.7
    assert rows[0]['seed_start']==2 and rows[0]['seed_end']==3
    assert rows[0]['seed_mean_pars']==1.5
    del table[2]
    assert list(window_records('ACGU',pars,table,4,2,1,1.))==[]
