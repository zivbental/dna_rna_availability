# YHL031C
Status: ok. Length: 707 nt. Measured usable bases: 389. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 389 | 0.3043 | 0.2694 |
| rnafold | ok | 389 | 0.3077 | 0.2821 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 139 | -0.1176 | -0.2681 |
| seed_p | 139 | -0.3958 | -0.3427 |
| seed_p_vs_seed_pars | 113 | -0.5494 | -0.6110 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
