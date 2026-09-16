# YLR059C
Status: ok. Length: 980 nt. Measured usable bases: 599. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 599 | 0.3502 | 0.3351 |
| rnafold | ok | 599 | 0.2793 | 0.2629 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 263 | -0.2441 | -0.1378 |
| seed_p | 263 | -0.3296 | -0.3748 |
| seed_p_vs_seed_pars | 177 | -0.3829 | -0.3404 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
