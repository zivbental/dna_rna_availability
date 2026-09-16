# YMR200W
Status: ok. Length: 1224 nt. Measured usable bases: 745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 745 | 0.3396 | 0.3345 |
| rnafold | ok | 745 | 0.2669 | 0.2741 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 291 | -0.2245 | -0.3403 |
| seed_p | 291 | -0.2565 | -0.2527 |
| seed_p_vs_seed_pars | 202 | -0.1058 | -0.0994 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
