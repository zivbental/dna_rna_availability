# YPR019W
Status: ok. Length: 3028 nt. Measured usable bases: 1286. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1286 | 0.2451 | 0.2306 |
| rnafold | ok | 1286 | 0.2313 | 0.2274 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | 0.0654 | -0.0850 |
| seed_p | 155 | 0.0175 | -0.0063 |
| seed_p_vs_seed_pars | 112 | 0.0501 | -0.0504 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
