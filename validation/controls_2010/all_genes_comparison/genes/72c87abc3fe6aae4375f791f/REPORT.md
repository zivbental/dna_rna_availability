# YML023C
Status: ok. Length: 1923 nt. Measured usable bases: 845. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 845 | 0.2568 | 0.2465 |
| rnafold | ok | 845 | 0.2120 | 0.2022 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.1399 | -0.1597 |
| seed_p | 137 | -0.1027 | 0.0195 |
| seed_p_vs_seed_pars | 102 | -0.3712 | -0.2646 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
