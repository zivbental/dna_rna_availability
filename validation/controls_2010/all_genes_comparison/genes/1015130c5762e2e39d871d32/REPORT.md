# YNL178W
Status: ok. Length: 808 nt. Measured usable bases: 769. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 769 | 0.3822 | 0.3887 |
| rnafold | ok | 769 | 0.3036 | 0.3008 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 747 | -0.2297 | -0.3379 |
| seed_p | 747 | -0.3670 | -0.3273 |
| seed_p_vs_seed_pars | 747 | -0.2380 | -0.2768 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
