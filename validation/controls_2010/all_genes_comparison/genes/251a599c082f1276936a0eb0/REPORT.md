# YEL066W
Status: ok. Length: 597 nt. Measured usable bases: 363. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 363 | 0.4130 | 0.4099 |
| rnafold | ok | 363 | 0.4074 | 0.3958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | -0.1894 | -0.2950 |
| seed_p | 155 | -0.3443 | -0.4628 |
| seed_p_vs_seed_pars | 118 | -0.1544 | -0.3394 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
