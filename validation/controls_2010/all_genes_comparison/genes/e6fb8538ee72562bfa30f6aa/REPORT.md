# YGL023C
Status: ok. Length: 2045 nt. Measured usable bases: 791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 791 | 0.3695 | 0.3575 |
| rnafold | ok | 791 | 0.3158 | 0.2876 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.5228 | -0.6565 |
| seed_p | 49 | -0.7660 | -0.6148 |
| seed_p_vs_seed_pars | 45 | -0.5246 | -0.2609 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
