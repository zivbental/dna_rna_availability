# YER063W
Status: ok. Length: 871 nt. Measured usable bases: 526. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 526 | 0.2990 | 0.3004 |
| rnafold | ok | 526 | 0.2288 | 0.2368 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 223 | -0.2040 | -0.3452 |
| seed_p | 223 | -0.3916 | -0.4233 |
| seed_p_vs_seed_pars | 175 | -0.5183 | -0.5391 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
