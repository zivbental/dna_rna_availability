# YLR248W
Status: ok. Length: 2110 nt. Measured usable bases: 1460. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1460 | 0.3224 | 0.3074 |
| rnafold | ok | 1460 | 0.2567 | 0.2527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 869 | -0.0436 | -0.0854 |
| seed_p | 869 | -0.1092 | -0.1271 |
| seed_p_vs_seed_pars | 664 | -0.1268 | -0.1432 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
