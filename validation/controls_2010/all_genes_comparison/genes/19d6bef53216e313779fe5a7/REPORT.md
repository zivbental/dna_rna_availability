# YBR265W
Status: ok. Length: 1143 nt. Measured usable bases: 778. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 778 | 0.3295 | 0.2999 |
| rnafold | ok | 778 | 0.2350 | 0.2192 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 441 | 0.1546 | 0.1214 |
| seed_p | 441 | -0.0564 | 0.0754 |
| seed_p_vs_seed_pars | 311 | 0.0070 | 0.1468 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
