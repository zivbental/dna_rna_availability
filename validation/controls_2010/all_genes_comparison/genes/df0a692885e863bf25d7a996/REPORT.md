# YKL085W
Status: ok. Length: 1511 nt. Measured usable bases: 993. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 993 | 0.3264 | 0.3277 |
| rnafold | ok | 993 | 0.3010 | 0.3068 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 652 | -0.1100 | -0.0746 |
| seed_p | 652 | -0.2418 | -0.2954 |
| seed_p_vs_seed_pars | 544 | -0.2936 | -0.3688 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
