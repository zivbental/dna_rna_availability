# YJR019C
Status: ok. Length: 1121 nt. Measured usable bases: 532. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 532 | 0.3250 | 0.3326 |
| rnafold | ok | 532 | 0.2983 | 0.2898 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.0269 | -0.0502 |
| seed_p | 67 | 0.0209 | -0.2012 |
| seed_p_vs_seed_pars | 59 | 0.1059 | -0.1852 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
