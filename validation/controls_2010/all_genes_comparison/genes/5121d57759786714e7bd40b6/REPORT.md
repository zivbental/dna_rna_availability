# YKL045W
Status: ok. Length: 1783 nt. Measured usable bases: 580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 580 | 0.4396 | 0.4380 |
| rnafold | ok | 580 | 0.3634 | 0.3951 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | 0.1814 | -0.1271 |
| seed_p | 42 | 0.3198 | 0.0273 |
| seed_p_vs_seed_pars | 33 | -0.1123 | -0.3469 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
