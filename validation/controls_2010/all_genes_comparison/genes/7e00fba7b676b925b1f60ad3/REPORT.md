# YHR033W
Status: ok. Length: 1322 nt. Measured usable bases: 654. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 654 | 0.2765 | 0.2573 |
| rnafold | ok | 654 | 0.1934 | 0.1736 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | 0.1612 | 0.0998 |
| seed_p | 147 | -0.1447 | -0.0566 |
| seed_p_vs_seed_pars | 77 | -0.1865 | -0.1157 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
