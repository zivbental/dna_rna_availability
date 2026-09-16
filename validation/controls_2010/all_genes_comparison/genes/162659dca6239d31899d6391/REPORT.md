# YBR177C
Status: ok. Length: 1473 nt. Measured usable bases: 961. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 961 | 0.3586 | 0.3283 |
| rnafold | ok | 961 | 0.2919 | 0.2569 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 504 | -0.0213 | -0.0530 |
| seed_p | 504 | -0.4382 | -0.3632 |
| seed_p_vs_seed_pars | 324 | -0.6144 | -0.5233 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
