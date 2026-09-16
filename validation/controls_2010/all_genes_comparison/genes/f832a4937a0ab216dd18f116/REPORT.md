# YGL220W
Status: ok. Length: 363 nt. Measured usable bases: 66. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 66 | 0.2846 | 0.1912 |
| rnafold | ok | 66 | 0.3574 | 0.2950 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.0837 | -0.2745 |
| seed_p | 39 | 0.1280 | 0.0894 |
| seed_p_vs_seed_pars | 29 | 0.4560 | 0.5510 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
