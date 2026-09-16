# YGL123W
Status: ok. Length: 952 nt. Measured usable bases: 902. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 902 | 0.3779 | 0.3768 |
| rnafold | ok | 902 | 0.3516 | 0.3498 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 881 | -0.0623 | -0.3815 |
| seed_p | 881 | -0.2197 | -0.3734 |
| seed_p_vs_seed_pars | 867 | -0.3516 | -0.4873 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
