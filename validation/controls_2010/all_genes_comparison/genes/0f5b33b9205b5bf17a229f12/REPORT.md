# YLR256W
Status: ok. Length: 4509 nt. Measured usable bases: 2412. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2412 | 0.2501 | 0.2503 |
| rnafold | ok | 2412 | 0.2233 | 0.2236 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 639 | -0.1781 | -0.1590 |
| seed_p | 639 | -0.2846 | -0.2455 |
| seed_p_vs_seed_pars | 470 | -0.2455 | -0.2086 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
