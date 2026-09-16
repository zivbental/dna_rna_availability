# YMR318C
Status: ok. Length: 1331 nt. Measured usable bases: 1145. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1145 | 0.2877 | 0.2703 |
| rnafold | ok | 1145 | 0.2186 | 0.2143 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1077 | -0.0919 | 0.1458 |
| seed_p | 1077 | -0.1167 | -0.0736 |
| seed_p_vs_seed_pars | 949 | -0.1333 | -0.1625 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
