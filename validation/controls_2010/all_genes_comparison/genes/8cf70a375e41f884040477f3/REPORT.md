# YER043C
Status: ok. Length: 1560 nt. Measured usable bases: 1387. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1387 | 0.3118 | 0.2854 |
| rnafold | ok | 1387 | 0.2331 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1310 | -0.2769 | 0.0304 |
| seed_p | 1310 | -0.2071 | -0.0740 |
| seed_p_vs_seed_pars | 1222 | -0.2987 | -0.1805 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
