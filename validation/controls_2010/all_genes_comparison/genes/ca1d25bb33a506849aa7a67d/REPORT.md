# YNL104C
Status: ok. Length: 1964 nt. Measured usable bases: 1416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1416 | 0.2462 | 0.2211 |
| rnafold | ok | 1416 | 0.1251 | 0.1219 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 949 | 0.0464 | 0.1130 |
| seed_p | 949 | -0.1119 | -0.0425 |
| seed_p_vs_seed_pars | 726 | -0.1604 | -0.1458 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
