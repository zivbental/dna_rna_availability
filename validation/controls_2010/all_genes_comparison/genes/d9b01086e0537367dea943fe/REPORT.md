# YER049W
Status: ok. Length: 2119 nt. Measured usable bases: 1448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1448 | 0.2757 | 0.2610 |
| rnafold | ok | 1448 | 0.2435 | 0.2287 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 884 | -0.0195 | -0.0939 |
| seed_p | 884 | -0.0465 | -0.0626 |
| seed_p_vs_seed_pars | 683 | -0.1629 | -0.2020 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
