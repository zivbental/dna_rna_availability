# YBL017C
Status: ok. Length: 4971 nt. Measured usable bases: 2484. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2484 | 0.3510 | 0.3393 |
| rnafold | ok | 2484 | 0.2976 | 0.3002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 489 | -0.1488 | -0.2494 |
| seed_p | 489 | -0.0260 | -0.1909 |
| seed_p_vs_seed_pars | 367 | -0.0874 | -0.2655 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
