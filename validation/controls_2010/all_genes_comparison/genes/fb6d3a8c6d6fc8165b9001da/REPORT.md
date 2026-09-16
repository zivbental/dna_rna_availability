# YDR399W
Status: ok. Length: 836 nt. Measured usable bases: 708. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 708 | 0.3657 | 0.3416 |
| rnafold | ok | 708 | 0.2692 | 0.2523 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 666 | -0.0306 | -0.1930 |
| seed_p | 666 | -0.4466 | -0.2927 |
| seed_p_vs_seed_pars | 561 | -0.4974 | -0.3121 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
