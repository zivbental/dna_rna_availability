# YLR216C
Status: ok. Length: 1180 nt. Measured usable bases: 959. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 959 | 0.3675 | 0.3659 |
| rnafold | ok | 959 | 0.3220 | 0.3327 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 766 | -0.2402 | -0.3262 |
| seed_p | 766 | -0.3334 | -0.3327 |
| seed_p_vs_seed_pars | 662 | -0.4109 | -0.3903 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
