# YDL103C
Status: ok. Length: 1583 nt. Measured usable bases: 960. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 960 | 0.3455 | 0.3287 |
| rnafold | ok | 960 | 0.3414 | 0.3255 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 301 | -0.1487 | 0.0345 |
| seed_p | 301 | -0.1932 | -0.0801 |
| seed_p_vs_seed_pars | 200 | -0.4920 | -0.3940 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
