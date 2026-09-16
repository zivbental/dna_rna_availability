# YGL037C
Status: ok. Length: 822 nt. Measured usable bases: 659. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 659 | 0.3670 | 0.3598 |
| rnafold | ok | 659 | 0.3190 | 0.3061 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 590 | -0.3527 | -0.2873 |
| seed_p | 590 | -0.4167 | -0.4336 |
| seed_p_vs_seed_pars | 509 | -0.4623 | -0.4166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
