# YGL031C
Status: ok. Length: 1064 nt. Measured usable bases: 417. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 417 | 0.3152 | 0.3131 |
| rnafold | ok | 417 | 0.1940 | 0.1937 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 196 | -0.2043 | -0.2855 |
| seed_p | 196 | -0.3370 | -0.4187 |
| seed_p_vs_seed_pars | 194 | -0.4794 | -0.5259 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
