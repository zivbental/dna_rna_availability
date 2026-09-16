# YOR021C
Status: ok. Length: 795 nt. Measured usable bases: 604. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 604 | 0.2750 | 0.2682 |
| rnafold | ok | 604 | 0.2561 | 0.2434 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 444 | -0.0585 | -0.1094 |
| seed_p | 444 | 0.0827 | -0.0931 |
| seed_p_vs_seed_pars | 378 | 0.0144 | -0.2248 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
