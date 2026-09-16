# YHR148W
Status: ok. Length: 879 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.2773 | 0.2757 |
| rnafold | ok | 399 | 0.2450 | 0.2361 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.2782 | -0.5857 |
| seed_p | 48 | -0.8045 | -0.8330 |
| seed_p_vs_seed_pars | 33 | -0.4205 | -0.9120 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
