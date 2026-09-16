# YDR174W
Status: ok. Length: 932 nt. Measured usable bases: 665. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 665 | 0.2410 | 0.2403 |
| rnafold | ok | 665 | 0.2644 | 0.2485 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 489 | -0.2395 | -0.2921 |
| seed_p | 489 | -0.2099 | -0.1231 |
| seed_p_vs_seed_pars | 428 | -0.0931 | -0.0080 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
