# YIL051C
Status: ok. Length: 565 nt. Measured usable bases: 518. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 518 | 0.2677 | 0.2425 |
| rnafold | ok | 518 | 0.3023 | 0.2775 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 504 | -0.0534 | -0.0005 |
| seed_p | 504 | -0.2318 | -0.1971 |
| seed_p_vs_seed_pars | 471 | -0.1648 | -0.2432 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
