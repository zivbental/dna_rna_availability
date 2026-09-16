# YFL037W
Status: ok. Length: 1666 nt. Measured usable bases: 1416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1416 | 0.2858 | 0.2612 |
| rnafold | ok | 1416 | 0.2853 | 0.2579 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1331 | -0.0601 | -0.3132 |
| seed_p | 1331 | -0.2529 | -0.2479 |
| seed_p_vs_seed_pars | 1145 | -0.3518 | -0.3446 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
