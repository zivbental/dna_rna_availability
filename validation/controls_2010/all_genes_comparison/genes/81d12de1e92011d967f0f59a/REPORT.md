# YKL157W
Status: ok. Length: 3034 nt. Measured usable bases: 2009. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2009 | 0.3524 | 0.3218 |
| rnafold | ok | 2009 | 0.2580 | 0.2404 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 935 | -0.0745 | -0.0957 |
| seed_p | 935 | -0.2756 | -0.2565 |
| seed_p_vs_seed_pars | 697 | -0.3780 | -0.3596 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
