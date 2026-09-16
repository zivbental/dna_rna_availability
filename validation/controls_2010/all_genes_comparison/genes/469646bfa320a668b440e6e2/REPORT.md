# YNL307C
Status: ok. Length: 1617 nt. Measured usable bases: 1208. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1208 | 0.2373 | 0.2264 |
| rnafold | ok | 1208 | 0.1806 | 0.1816 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 940 | 0.0115 | -0.0461 |
| seed_p | 940 | -0.1126 | -0.1663 |
| seed_p_vs_seed_pars | 778 | -0.3253 | -0.3349 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
