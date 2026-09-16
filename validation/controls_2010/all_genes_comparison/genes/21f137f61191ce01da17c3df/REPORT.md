# YKR062W
Status: ok. Length: 1166 nt. Measured usable bases: 522. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 522 | 0.3905 | 0.3738 |
| rnafold | ok | 522 | 0.3291 | 0.3133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | 0.6136 | 0.7284 |
| seed_p | 55 | 0.4363 | 0.5275 |
| seed_p_vs_seed_pars | 42 | 0.6484 | 0.7362 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
