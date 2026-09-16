# YLR266C
Status: ok. Length: 2106 nt. Measured usable bases: 806. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 806 | 0.3096 | 0.2965 |
| rnafold | ok | 806 | 0.2547 | 0.2614 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.1881 | 0.0543 |
| seed_p | 39 | -0.3271 | -0.2549 |
| seed_p_vs_seed_pars | 23 | -0.6079 | -0.5491 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
