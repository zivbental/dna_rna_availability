# YGR065C
Status: ok. Length: 1992 nt. Measured usable bases: 940. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 940 | 0.2369 | 0.2403 |
| rnafold | ok | 940 | 0.2288 | 0.2461 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | -0.1896 | 0.0149 |
| seed_p | 122 | 0.1327 | 0.1500 |
| seed_p_vs_seed_pars | 77 | -0.1503 | 0.0229 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
