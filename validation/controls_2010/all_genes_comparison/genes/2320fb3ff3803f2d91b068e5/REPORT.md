# YHR064C
Status: ok. Length: 1720 nt. Measured usable bases: 1562. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1562 | 0.3687 | 0.3561 |
| rnafold | ok | 1562 | 0.2714 | 0.2570 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1494 | -0.2871 | -0.1956 |
| seed_p | 1494 | -0.2509 | -0.2460 |
| seed_p_vs_seed_pars | 1432 | -0.4909 | -0.4577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
