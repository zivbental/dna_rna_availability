# YGR240C
Status: ok. Length: 3393 nt. Measured usable bases: 2925. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2925 | 0.2812 | 0.2663 |
| rnafold | ok | 2925 | 0.2565 | 0.2588 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2739 | -0.1165 | -0.0118 |
| seed_p | 2739 | -0.0261 | 0.0269 |
| seed_p_vs_seed_pars | 2456 | -0.0950 | -0.0320 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
