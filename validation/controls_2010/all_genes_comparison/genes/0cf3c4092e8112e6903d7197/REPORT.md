# YKL135C
Status: ok. Length: 2334 nt. Measured usable bases: 1120. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1120 | 0.3682 | 0.3700 |
| rnafold | ok | 1120 | 0.2825 | 0.2751 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | -0.2082 | -0.2556 |
| seed_p | 162 | -0.2086 | -0.2468 |
| seed_p_vs_seed_pars | 118 | -0.3518 | -0.3508 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
