# YDR517W
Status: ok. Length: 1371 nt. Measured usable bases: 948. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 948 | 0.3225 | 0.3063 |
| rnafold | ok | 948 | 0.2311 | 0.2412 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 520 | 0.1139 | 0.1899 |
| seed_p | 520 | -0.2310 | -0.2646 |
| seed_p_vs_seed_pars | 411 | -0.3264 | -0.3439 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
