# YLR104W
Status: ok. Length: 500 nt. Measured usable bases: 271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.1506 | 0.1505 |
| rnafold | ok | 271 | 0.1519 | 0.1531 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.1593 | 0.6929 |
| seed_p | 67 | -0.2801 | -0.2586 |
| seed_p_vs_seed_pars | 39 | -0.1251 | 0.1289 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
