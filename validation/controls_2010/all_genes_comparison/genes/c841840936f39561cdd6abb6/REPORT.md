# YOR052C
Status: ok. Length: 814 nt. Measured usable bases: 425. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.3800 | 0.3633 |
| rnafold | ok | 425 | 0.2992 | 0.3077 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 164 | -0.2030 | -0.0287 |
| seed_p | 164 | -0.0080 | 0.0571 |
| seed_p_vs_seed_pars | 98 | -0.5805 | -0.6582 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
