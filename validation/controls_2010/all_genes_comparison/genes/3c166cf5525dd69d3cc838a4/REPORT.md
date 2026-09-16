# YBL076C
Status: ok. Length: 3301 nt. Measured usable bases: 2725. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2725 | 0.3135 | 0.2833 |
| rnafold | ok | 2725 | 0.2192 | 0.2185 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2339 | -0.0445 | -0.1421 |
| seed_p | 2339 | -0.0228 | -0.0275 |
| seed_p_vs_seed_pars | 1892 | -0.0787 | -0.1183 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
