# YDR221W
Status: ok. Length: 2314 nt. Measured usable bases: 920. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 920 | 0.2595 | 0.2523 |
| rnafold | ok | 920 | 0.1997 | 0.2038 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.5442 | 0.6449 |
| seed_p | 66 | 0.5486 | 0.6953 |
| seed_p_vs_seed_pars | 45 | 0.0510 | 0.2515 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
