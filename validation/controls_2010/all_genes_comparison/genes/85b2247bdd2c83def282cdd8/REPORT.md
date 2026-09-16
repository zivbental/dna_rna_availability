# YOL042W
Status: ok. Length: 1443 nt. Measured usable bases: 507. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 507 | 0.3279 | 0.3262 |
| rnafold | ok | 507 | 0.2713 | 0.2612 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | 0.0179 | -0.4104 |
| seed_p | 46 | -0.3619 | -0.2145 |
| seed_p_vs_seed_pars | 29 | -0.7693 | -0.7309 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
