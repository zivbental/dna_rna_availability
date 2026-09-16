# YDL055C
Status: ok. Length: 1458 nt. Measured usable bases: 1335. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1335 | 0.3199 | 0.3113 |
| rnafold | ok | 1335 | 0.2358 | 0.2352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1301 | 0.0170 | -0.1301 |
| seed_p | 1301 | -0.1559 | -0.1669 |
| seed_p_vs_seed_pars | 1258 | -0.2560 | -0.2275 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
