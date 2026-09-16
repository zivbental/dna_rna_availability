# YDR155C
Status: ok. Length: 610 nt. Measured usable bases: 548. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 548 | 0.3878 | 0.3800 |
| rnafold | ok | 548 | 0.3799 | 0.3757 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 495 | -0.3361 | -0.0898 |
| seed_p | 495 | -0.3926 | -0.3436 |
| seed_p_vs_seed_pars | 486 | -0.3856 | -0.3747 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
