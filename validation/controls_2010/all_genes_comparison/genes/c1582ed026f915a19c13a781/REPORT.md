# YJL190C
Status: ok. Length: 534 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.4573 | 0.4644 |
| rnafold | ok | 402 | 0.4012 | 0.4189 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 330 | -0.2193 | -0.4956 |
| seed_p | 330 | -0.3327 | -0.4177 |
| seed_p_vs_seed_pars | 294 | -0.5241 | -0.6010 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
