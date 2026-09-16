# YML028W
Status: ok. Length: 730 nt. Measured usable bases: 547. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 547 | 0.2696 | 0.2779 |
| rnafold | ok | 547 | 0.2163 | 0.2101 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 543 | -0.1261 | -0.3291 |
| seed_p | 543 | -0.3119 | -0.3765 |
| seed_p_vs_seed_pars | 541 | -0.2244 | -0.3407 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
