# YNL239W
Status: ok. Length: 1565 nt. Measured usable bases: 1158. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1158 | 0.2604 | 0.2292 |
| rnafold | ok | 1158 | 0.2378 | 0.2070 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 857 | -0.0883 | 0.0456 |
| seed_p | 857 | -0.0964 | -0.0090 |
| seed_p_vs_seed_pars | 661 | -0.2834 | -0.1448 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
