# YMR186W
Status: ok. Length: 2234 nt. Measured usable bases: 1487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1487 | 0.3256 | 0.3170 |
| rnafold | ok | 1487 | 0.2790 | 0.2638 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1089 | -0.1221 | -0.2269 |
| seed_p | 1089 | -0.1663 | -0.0768 |
| seed_p_vs_seed_pars | 937 | -0.2368 | -0.1233 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
