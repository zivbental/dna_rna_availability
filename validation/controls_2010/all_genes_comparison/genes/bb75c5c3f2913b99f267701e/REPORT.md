# YOL077C
Status: ok. Length: 971 nt. Measured usable bases: 645. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 645 | 0.2825 | 0.3051 |
| rnafold | ok | 645 | 0.2233 | 0.2460 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 318 | -0.3019 | -0.3051 |
| seed_p | 318 | -0.4698 | -0.3358 |
| seed_p_vs_seed_pars | 267 | -0.2338 | -0.2072 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
