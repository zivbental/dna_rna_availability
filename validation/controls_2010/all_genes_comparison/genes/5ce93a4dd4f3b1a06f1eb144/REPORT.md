# YEL047C
Status: ok. Length: 1507 nt. Measured usable bases: 1062. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1062 | 0.3444 | 0.3335 |
| rnafold | ok | 1062 | 0.3044 | 0.3019 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 671 | -0.1020 | -0.0408 |
| seed_p | 671 | -0.1161 | -0.0521 |
| seed_p_vs_seed_pars | 577 | -0.3286 | -0.2191 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
