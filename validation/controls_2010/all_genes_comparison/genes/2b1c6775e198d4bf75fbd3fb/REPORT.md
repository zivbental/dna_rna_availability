# YJR075W
Status: ok. Length: 1438 nt. Measured usable bases: 978. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 978 | 0.3324 | 0.3319 |
| rnafold | ok | 978 | 0.3062 | 0.3027 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 694 | -0.0269 | -0.0407 |
| seed_p | 694 | -0.1081 | -0.1183 |
| seed_p_vs_seed_pars | 603 | -0.1260 | -0.1234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
