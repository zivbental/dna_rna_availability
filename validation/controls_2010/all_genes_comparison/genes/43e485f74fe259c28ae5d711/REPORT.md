# YGL028C
Status: ok. Length: 2063 nt. Measured usable bases: 1452. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1452 | 0.2460 | 0.2320 |
| rnafold | ok | 1452 | 0.1964 | 0.1852 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 888 | 0.0491 | -0.0213 |
| seed_p | 888 | -0.1164 | -0.1055 |
| seed_p_vs_seed_pars | 719 | -0.1655 | -0.1018 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
