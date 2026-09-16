# YNL243W
Status: ok. Length: 3018 nt. Measured usable bases: 2163. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2163 | 0.3596 | 0.3524 |
| rnafold | ok | 2163 | 0.3328 | 0.3240 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1457 | 0.0059 | -0.2117 |
| seed_p | 1457 | -0.1813 | -0.2243 |
| seed_p_vs_seed_pars | 1241 | -0.3478 | -0.2900 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
