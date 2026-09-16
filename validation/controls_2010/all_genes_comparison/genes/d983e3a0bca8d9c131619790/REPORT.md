# YPL221W
Status: ok. Length: 2576 nt. Measured usable bases: 1548. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1548 | 0.3249 | 0.3001 |
| rnafold | ok | 1548 | 0.1885 | 0.1765 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 598 | -0.1052 | -0.0107 |
| seed_p | 598 | -0.2579 | -0.1307 |
| seed_p_vs_seed_pars | 483 | -0.3463 | -0.2814 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
