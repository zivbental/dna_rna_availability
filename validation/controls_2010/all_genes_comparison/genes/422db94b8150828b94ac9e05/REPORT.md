# YKL060C
Status: ok. Length: 1119 nt. Measured usable bases: 1093. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1093 | 0.3831 | 0.3693 |
| rnafold | ok | 1093 | 0.3321 | 0.3243 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1080 | 0.0059 | -0.1006 |
| seed_p | 1080 | -0.1847 | -0.1046 |
| seed_p_vs_seed_pars | 1080 | -0.2766 | -0.1999 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
