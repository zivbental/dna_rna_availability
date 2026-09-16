# YOR004W
Status: ok. Length: 958 nt. Measured usable bases: 517. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 517 | 0.4040 | 0.4158 |
| rnafold | ok | 517 | 0.3429 | 0.3436 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | 0.3399 | 0.5931 |
| seed_p | 90 | 0.0772 | 0.2282 |
| seed_p_vs_seed_pars | 64 | -0.3016 | -0.2263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
