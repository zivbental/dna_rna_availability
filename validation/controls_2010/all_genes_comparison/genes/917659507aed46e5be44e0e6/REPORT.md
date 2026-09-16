# YOL030W
Status: ok. Length: 1675 nt. Measured usable bases: 1344. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1344 | 0.3070 | 0.2950 |
| rnafold | ok | 1344 | 0.2317 | 0.2363 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1091 | -0.1241 | -0.1309 |
| seed_p | 1091 | -0.1458 | -0.1202 |
| seed_p_vs_seed_pars | 994 | -0.1771 | -0.1878 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
