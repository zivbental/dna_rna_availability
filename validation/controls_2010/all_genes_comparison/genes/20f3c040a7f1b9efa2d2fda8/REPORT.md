# YKL117W
Status: ok. Length: 827 nt. Measured usable bases: 644. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 644 | 0.3610 | 0.3657 |
| rnafold | ok | 644 | 0.3672 | 0.3708 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 576 | -0.2743 | -0.1664 |
| seed_p | 576 | -0.0991 | -0.0328 |
| seed_p_vs_seed_pars | 547 | -0.1382 | -0.0683 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
