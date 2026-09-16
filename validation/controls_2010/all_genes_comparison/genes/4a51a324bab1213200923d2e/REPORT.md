# YDL135C
Status: ok. Length: 841 nt. Measured usable bases: 416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 416 | 0.3447 | 0.3350 |
| rnafold | ok | 416 | 0.2906 | 0.2898 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | 0.1798 | 0.1703 |
| seed_p | 97 | 0.1314 | -0.0002 |
| seed_p_vs_seed_pars | 70 | -0.3504 | -0.5562 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
