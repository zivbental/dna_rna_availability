# YBR015C
Status: ok. Length: 2031 nt. Measured usable bases: 1428.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1428 | 0.3206 | 0.3144 |
| rnafold | ok | 1428 | 0.3051 | 0.2990 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 890 | -0.1095 | -0.0947 |
| seed_p | 890 | -0.0349 | -0.0461 |
| seed_p_vs_seed_pars | 630 | -0.2426 | -0.2288 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
