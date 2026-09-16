# YOL126C
Status: ok. Length: 1514 nt. Measured usable bases: 576. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 576 | 0.3541 | 0.3327 |
| rnafold | ok | 576 | 0.2358 | 0.2238 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.0252 | -0.1533 |
| seed_p | 43 | -0.0093 | -0.0316 |
| seed_p_vs_seed_pars | 22 | 0.0037 | 0.0240 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
