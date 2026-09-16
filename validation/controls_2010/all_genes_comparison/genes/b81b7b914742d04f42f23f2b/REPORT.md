# YDR208W
Status: ok. Length: 2492 nt. Measured usable bases: 991. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 991 | 0.3348 | 0.3094 |
| rnafold | ok | 991 | 0.2964 | 0.2786 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 100 | -0.2436 | -0.4113 |
| seed_p | 100 | -0.5153 | -0.2736 |
| seed_p_vs_seed_pars | 89 | -0.4314 | -0.1557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
