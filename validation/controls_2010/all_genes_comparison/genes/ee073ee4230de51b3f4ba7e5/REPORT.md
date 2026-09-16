# YMR308C
Status: ok. Length: 3429 nt. Measured usable bases: 2369. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2369 | 0.2788 | 0.2734 |
| rnafold | ok | 2369 | 0.2576 | 0.2549 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1303 | 0.0320 | -0.0752 |
| seed_p | 1303 | -0.1352 | -0.1845 |
| seed_p_vs_seed_pars | 1074 | -0.0862 | -0.1366 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
