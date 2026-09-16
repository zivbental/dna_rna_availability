# All-transcript Kertesz 2010 comparison

Selected deposited transcripts: 3196. Status counts: {'ok': 2936, 'insufficient_measurements': 10, 'failed': 250}.

| Comparison | Matched observations | Pooled Pearson | Median per-gene Pearson | Median per-gene Spearman |
| --- | --- | --- | --- | --- |
| per_base:rnafold | 2384855 | 0.2583 | 0.2676 | 0.2635 |
| per_base:rnaplfold | 2384855 | 0.3076 | 0.3142 | 0.3039 |
| window:full_p | 1062244 | -0.0630 | -0.0857 | -0.1129 |
| window:seed_p | 1062244 | -0.1686 | -0.1729 | -0.1522 |
| window:seed_p_vs_seed_pars | 865856 | -0.2547 | -0.2614 | -0.2393 |

Per-base comparisons match experimental PARS with predicted pairing probability (expected positive association). Local-window diagnostics compare mean PARS with 20-nt joint opening and the best contiguous 8-nt seed (expected negative tendency); actual footprint/seed settings are recorded in the manifest. These diagnostics are not validation of joint opening, binding or strand displacement. No experimental values constrain the predictions.

Pooled Pearson weights long, well-covered transcripts more heavily and combines within- and between-transcript effects. Median per-gene correlations give a complementary view with equal weight per defined gene correlation. Pooled Spearman and significance tests are deliberately absent: nearby bases, overlapping transcripts/windows and seed selection violate simple independence assumptions. No genome-wide accuracy claim follows from a handful of illustrative windows.

Missing PARS entries remain missing; measured zero is preserved. Default handling excludes measured positions overlapping an oppositely oriented annotated transcript because the deposited WIG has no strand label. Input sequences must exactly reconstruct from the matching sacCer2 contiguous interval or deposited exon/UTR blocks before use; removed genomic segments do not receive RNA positions. Skipped genes and model failures remain visible; no length ceiling is applied unless explicitly requested. All deposited transcript records are considered, including noncoding records; this is not every genomic yeast gene. Experimental buffer and temperature are not asserted to match the computational conditions.

[Per-gene table and individual report links](per_gene.tsv) · [Aggregate statistics](summary.json) · [Provenance and settings](manifest.json)
