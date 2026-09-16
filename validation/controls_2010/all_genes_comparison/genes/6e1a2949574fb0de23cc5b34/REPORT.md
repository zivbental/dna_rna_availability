# YNR027W
Status: ok. Length: 1235 nt. Measured usable bases: 572. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 572 | 0.2851 | 0.2686 |
| rnafold | ok | 572 | 0.2488 | 0.2488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | 0.0015 | 0.1519 |
| seed_p | 121 | -0.1149 | -0.0987 |
| seed_p_vs_seed_pars | 89 | 0.0152 | 0.2719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
