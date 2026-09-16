# YML072C
Status: ok. Length: 4931 nt. Measured usable bases: 3047. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3047 | 0.3407 | 0.3303 |
| rnafold | ok | 3047 | 0.3221 | 0.3081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1258 | -0.1896 | -0.0444 |
| seed_p | 1258 | -0.1986 | -0.1312 |
| seed_p_vs_seed_pars | 856 | -0.3868 | -0.3423 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
