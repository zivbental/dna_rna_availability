# YEL040W
Status: ok. Length: 1538 nt. Measured usable bases: 1330. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1330 | 0.2366 | 0.2167 |
| rnafold | ok | 1330 | 0.1437 | 0.1237 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1274 | 0.0002 | 0.0881 |
| seed_p | 1274 | -0.0792 | -0.0198 |
| seed_p_vs_seed_pars | 1080 | -0.1709 | -0.2004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
