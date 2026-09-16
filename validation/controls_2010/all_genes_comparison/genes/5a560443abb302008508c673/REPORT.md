# YFL041W
Status: ok. Length: 2055 nt. Measured usable bases: 1218. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1218 | 0.3091 | 0.2869 |
| rnafold | ok | 1218 | 0.2063 | 0.1896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 456 | -0.0044 | 0.0014 |
| seed_p | 456 | 0.0339 | 0.0576 |
| seed_p_vs_seed_pars | 368 | -0.1654 | -0.1301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
