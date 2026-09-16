# YLR242C
Status: ok. Length: 966 nt. Measured usable bases: 434. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 434 | 0.3286 | 0.3271 |
| rnafold | ok | 434 | 0.3063 | 0.3219 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | 0.4386 | 0.2523 |
| seed_p | 61 | 0.0026 | 0.0969 |
| seed_p_vs_seed_pars | 49 | -0.2626 | -0.1944 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
