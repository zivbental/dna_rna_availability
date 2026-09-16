# YNL294C
Status: ok. Length: 1910 nt. Measured usable bases: 1003. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.2681 | 0.2818 |
| rnafold | ok | 1003 | 0.2072 | 0.2371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 286 | -0.0036 | -0.0687 |
| seed_p | 286 | -0.1281 | -0.1882 |
| seed_p_vs_seed_pars | 243 | -0.3207 | -0.3738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
