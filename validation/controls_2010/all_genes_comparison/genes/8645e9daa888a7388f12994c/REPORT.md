# YDL202W
Status: ok. Length: 887 nt. Measured usable bases: 342. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 342 | 0.3014 | 0.2881 |
| rnafold | ok | 342 | 0.3510 | 0.3158 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.7132 | -0.8336 |
| seed_p | 37 | -0.7157 | -0.4747 |
| seed_p_vs_seed_pars | 34 | -0.6474 | -0.3307 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
