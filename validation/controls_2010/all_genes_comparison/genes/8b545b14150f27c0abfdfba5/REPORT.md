# YNR028W
Status: ok. Length: 1019 nt. Measured usable bases: 645. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 645 | 0.2936 | 0.2940 |
| rnafold | ok | 645 | 0.1892 | 0.2008 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 306 | -0.0459 | 0.0793 |
| seed_p | 306 | -0.1600 | -0.1235 |
| seed_p_vs_seed_pars | 272 | -0.2962 | -0.2809 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
