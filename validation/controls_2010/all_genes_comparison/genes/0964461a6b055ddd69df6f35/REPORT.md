# YFL016C
Status: ok. Length: 1631 nt. Measured usable bases: 839. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 839 | 0.3465 | 0.3340 |
| rnafold | ok | 839 | 0.2706 | 0.2602 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 240 | -0.1581 | -0.2473 |
| seed_p | 240 | -0.2728 | -0.3089 |
| seed_p_vs_seed_pars | 167 | -0.5209 | -0.3998 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
