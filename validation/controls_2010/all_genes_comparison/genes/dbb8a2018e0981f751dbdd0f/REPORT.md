# YJR104C
Status: ok. Length: 542 nt. Measured usable bases: 485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 485 | 0.3511 | 0.3213 |
| rnafold | ok | 485 | 0.2430 | 0.1959 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 478 | -0.3742 | -0.3340 |
| seed_p | 478 | -0.2463 | -0.1541 |
| seed_p_vs_seed_pars | 474 | -0.2705 | -0.2411 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
