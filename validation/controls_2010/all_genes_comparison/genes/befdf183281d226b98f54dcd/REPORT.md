# YKL138C
Status: ok. Length: 546 nt. Measured usable bases: 225. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 225 | 0.3166 | 0.3343 |
| rnafold | ok | 225 | 0.2858 | 0.3005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | 0.2530 | 0.3306 |
| seed_p | 30 | 0.8687 | 0.7660 |
| seed_p_vs_seed_pars | 8 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
