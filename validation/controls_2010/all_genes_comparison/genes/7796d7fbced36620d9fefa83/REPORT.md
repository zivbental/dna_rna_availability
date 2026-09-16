# YPL028W
Status: ok. Length: 1333 nt. Measured usable bases: 1191. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1191 | 0.3472 | 0.3440 |
| rnafold | ok | 1191 | 0.2992 | 0.2958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1150 | -0.0497 | -0.1216 |
| seed_p | 1150 | -0.2406 | -0.2924 |
| seed_p_vs_seed_pars | 1071 | -0.2148 | -0.2518 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
