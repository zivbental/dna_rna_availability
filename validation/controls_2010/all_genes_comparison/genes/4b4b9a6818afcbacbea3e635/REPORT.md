# YNL061W
Status: ok. Length: 2036 nt. Measured usable bases: 943. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 943 | 0.3421 | 0.3496 |
| rnafold | ok | 943 | 0.3399 | 0.3354 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | -0.0486 | -0.2283 |
| seed_p | 165 | -0.1935 | -0.1917 |
| seed_p_vs_seed_pars | 125 | -0.2357 | -0.3366 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
