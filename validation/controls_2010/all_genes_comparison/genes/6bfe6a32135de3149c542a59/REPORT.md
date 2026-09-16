# YKL024C
Status: ok. Length: 923 nt. Measured usable bases: 519. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 519 | 0.3083 | 0.2868 |
| rnafold | ok | 519 | 0.3178 | 0.2944 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 369 | -0.0734 | -0.1777 |
| seed_p | 369 | -0.1590 | -0.2087 |
| seed_p_vs_seed_pars | 302 | -0.3670 | -0.3610 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
