# YOL110W
Status: ok. Length: 898 nt. Measured usable bases: 441. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 441 | 0.3456 | 0.3436 |
| rnafold | ok | 441 | 0.2337 | 0.2606 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | 0.4455 | 0.4940 |
| seed_p | 77 | 0.0344 | 0.0835 |
| seed_p_vs_seed_pars | 38 | 0.1198 | 0.5653 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
