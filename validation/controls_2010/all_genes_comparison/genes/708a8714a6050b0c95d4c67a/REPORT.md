# YDR513W
Status: ok. Length: 534 nt. Measured usable bases: 352. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 352 | 0.2612 | 0.2559 |
| rnafold | ok | 352 | 0.2499 | 0.2456 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | -0.3501 | -0.3757 |
| seed_p | 249 | -0.4785 | -0.4685 |
| seed_p_vs_seed_pars | 165 | -0.3960 | -0.3796 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
