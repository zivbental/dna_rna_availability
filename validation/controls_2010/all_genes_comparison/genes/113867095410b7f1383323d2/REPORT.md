# YHR103W
Status: ok. Length: 2677 nt. Measured usable bases: 1326. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1326 | 0.3039 | 0.2957 |
| rnafold | ok | 1326 | 0.2516 | 0.2528 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 260 | 0.0840 | 0.0185 |
| seed_p | 260 | -0.1183 | -0.0379 |
| seed_p_vs_seed_pars | 170 | -0.2089 | -0.0293 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
