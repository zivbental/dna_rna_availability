# YER150W
Status: ok. Length: 633 nt. Measured usable bases: 240. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 240 | 0.1310 | 0.1288 |
| rnafold | ok | 240 | 0.1793 | 0.1908 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.8306 | 0.1620 |
| seed_p | 25 | 0.7908 | 0.5993 |
| seed_p_vs_seed_pars | 13 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
