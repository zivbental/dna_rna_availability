# YDR462W
Status: ok. Length: 606 nt. Measured usable bases: 291. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 291 | 0.3798 | 0.3544 |
| rnafold | ok | 291 | 0.3528 | 0.3458 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | -0.2724 | -0.5829 |
| seed_p | 50 | -0.2398 | -0.3440 |
| seed_p_vs_seed_pars | 33 | -0.2096 | 0.2021 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
