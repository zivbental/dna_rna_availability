# YDR061W
Status: ok. Length: 1788 nt. Measured usable bases: 655. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 655 | 0.2818 | 0.2809 |
| rnafold | ok | 655 | 0.2645 | 0.2536 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | 0.3750 | 0.5255 |
| seed_p | 45 | 0.2878 | 0.4275 |
| seed_p_vs_seed_pars | 30 | 0.1998 | -0.1795 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
