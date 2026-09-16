# YDL180W
Status: ok. Length: 2063 nt. Measured usable bases: 845. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 845 | 0.2690 | 0.2635 |
| rnafold | ok | 845 | 0.2589 | 0.2509 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | 0.1939 | -0.0421 |
| seed_p | 157 | -0.1908 | -0.1828 |
| seed_p_vs_seed_pars | 110 | -0.0291 | 0.0416 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
