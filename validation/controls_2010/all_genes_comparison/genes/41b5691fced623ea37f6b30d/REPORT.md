# YLR305C
Status: ok. Length: 5754 nt. Measured usable bases: 2423. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2423 | 0.2940 | 0.2785 |
| rnafold | ok | 2423 | 0.2118 | 0.2131 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 224 | -0.0065 | -0.0310 |
| seed_p | 224 | -0.3580 | -0.1569 |
| seed_p_vs_seed_pars | 171 | -0.5541 | -0.3389 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
