# YBR221C
Status: ok. Length: 1518 nt. Measured usable bases: 1361. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1361 | 0.3174 | 0.3031 |
| rnafold | ok | 1361 | 0.1942 | 0.2004 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1338 | -0.0820 | -0.1561 |
| seed_p | 1338 | -0.3101 | -0.2676 |
| seed_p_vs_seed_pars | 1205 | -0.3832 | -0.3651 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
