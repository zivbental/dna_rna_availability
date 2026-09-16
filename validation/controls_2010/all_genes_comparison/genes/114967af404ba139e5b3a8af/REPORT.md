# YDL235C
Status: ok. Length: 730 nt. Measured usable bases: 335. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 335 | 0.3325 | 0.3339 |
| rnafold | ok | 335 | 0.4283 | 0.4371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | -0.0784 | -0.0450 |
| seed_p | 141 | -0.0623 | -0.0541 |
| seed_p_vs_seed_pars | 93 | -0.1056 | -0.0468 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
