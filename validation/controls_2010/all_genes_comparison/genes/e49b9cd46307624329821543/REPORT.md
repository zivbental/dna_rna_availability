# YJR121W
Status: ok. Length: 1607 nt. Measured usable bases: 1484. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1484 | 0.3052 | 0.2934 |
| rnafold | ok | 1484 | 0.2441 | 0.2267 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1538 | -0.0722 | -0.2014 |
| seed_p | 1538 | -0.1220 | -0.2079 |
| seed_p_vs_seed_pars | 1378 | -0.1956 | -0.2935 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
