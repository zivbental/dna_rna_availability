# YHR067W
Status: ok. Length: 1199 nt. Measured usable bases: 479. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 479 | 0.3544 | 0.3321 |
| rnafold | ok | 479 | 0.3215 | 0.3185 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.1611 | -0.0752 |
| seed_p | 34 | -0.2219 | 0.0686 |
| seed_p_vs_seed_pars | 31 | 0.2327 | 0.4014 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
