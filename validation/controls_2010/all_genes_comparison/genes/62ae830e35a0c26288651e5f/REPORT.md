# YOR354C
Status: ok. Length: 2260 nt. Measured usable bases: 927. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 927 | 0.2519 | 0.2506 |
| rnafold | ok | 927 | 0.2430 | 0.2349 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 104 | 0.0542 | 0.2237 |
| seed_p | 104 | -0.2516 | -0.0815 |
| seed_p_vs_seed_pars | 79 | -0.0402 | -0.0463 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
