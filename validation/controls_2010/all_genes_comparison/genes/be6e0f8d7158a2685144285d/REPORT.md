# YOR016C
Status: ok. Length: 832 nt. Measured usable bases: 512. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 512 | 0.1905 | 0.1790 |
| rnafold | ok | 512 | 0.1500 | 0.1655 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 251 | 0.0081 | -0.1200 |
| seed_p | 251 | 0.1457 | -0.0149 |
| seed_p_vs_seed_pars | 210 | 0.0432 | -0.0711 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
