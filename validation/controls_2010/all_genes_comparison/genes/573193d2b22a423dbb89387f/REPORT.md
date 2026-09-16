# YPL215W
Status: ok. Length: 1186 nt. Measured usable bases: 500. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 500 | 0.3180 | 0.2877 |
| rnafold | ok | 500 | 0.2998 | 0.2838 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.5754 | -0.7448 |
| seed_p | 57 | -0.7802 | -0.7937 |
| seed_p_vs_seed_pars | 42 | -0.8175 | -0.8190 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
