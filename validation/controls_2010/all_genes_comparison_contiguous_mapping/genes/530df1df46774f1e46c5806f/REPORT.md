# YAL043C
Status: ok. Length: 2466 nt. Measured usable bases: 1275.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1275 | 0.3585 | 0.3423 |
| rnafold | ok | 1275 | 0.3014 | 0.2955 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 341 | -0.0522 | -0.1993 |
| seed_p | 341 | -0.4579 | -0.4968 |
| seed_p_vs_seed_pars | 226 | -0.5992 | -0.5573 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
