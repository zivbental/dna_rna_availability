# YNL310C
Status: ok. Length: 603 nt. Measured usable bases: 372. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 372 | 0.3514 | 0.3293 |
| rnafold | ok | 372 | 0.2550 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | 0.1214 | 0.1950 |
| seed_p | 132 | -0.4993 | -0.3290 |
| seed_p_vs_seed_pars | 125 | -0.5721 | -0.3771 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
