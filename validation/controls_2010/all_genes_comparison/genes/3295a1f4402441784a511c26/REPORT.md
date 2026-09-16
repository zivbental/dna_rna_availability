# YNR033W
Status: ok. Length: 2456 nt. Measured usable bases: 1081. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1081 | 0.3019 | 0.2905 |
| rnafold | ok | 1081 | 0.2497 | 0.2559 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | -0.4903 | -0.4870 |
| seed_p | 150 | -0.1293 | -0.1993 |
| seed_p_vs_seed_pars | 114 | -0.1454 | -0.2246 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
