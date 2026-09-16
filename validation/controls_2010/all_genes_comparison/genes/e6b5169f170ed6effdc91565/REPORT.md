# YLL009C
Status: ok. Length: 335 nt. Measured usable bases: 221. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 221 | 0.2385 | 0.2358 |
| rnafold | ok | 221 | 0.2925 | 0.3062 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | 0.0504 | 0.1726 |
| seed_p | 109 | -0.0239 | -0.0622 |
| seed_p_vs_seed_pars | 79 | -0.0365 | -0.2173 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
