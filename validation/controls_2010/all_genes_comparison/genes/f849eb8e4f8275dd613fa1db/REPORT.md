# YBR193C
Status: ok. Length: 963 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.3407 | 0.3236 |
| rnafold | ok | 401 | 0.2551 | 0.2387 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.8180 | -0.6920 |
| seed_p | 54 | -0.5859 | -0.4518 |
| seed_p_vs_seed_pars | 47 | -0.3998 | -0.1558 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
