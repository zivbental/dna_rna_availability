# YGL012W
Status: ok. Length: 1552 nt. Measured usable bases: 1376. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1376 | 0.2885 | 0.2715 |
| rnafold | ok | 1376 | 0.2652 | 0.2554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1299 | -0.0387 | -0.1118 |
| seed_p | 1299 | -0.1471 | -0.1890 |
| seed_p_vs_seed_pars | 1220 | -0.2430 | -0.2640 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
