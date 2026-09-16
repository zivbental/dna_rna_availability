# YDR093W
Status: ok. Length: 4839 nt. Measured usable bases: 1989. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1989 | 0.3183 | 0.2966 |
| rnafold | ok | 1989 | 0.2779 | 0.2627 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 367 | -0.0070 | 0.2254 |
| seed_p | 367 | -0.1030 | -0.1731 |
| seed_p_vs_seed_pars | 294 | -0.2496 | -0.2492 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
