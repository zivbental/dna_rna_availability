# YOR236W
Status: ok. Length: 700 nt. Measured usable bases: 355. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 355 | 0.4293 | 0.4129 |
| rnafold | ok | 355 | 0.2686 | 0.2393 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.5109 | -0.5547 |
| seed_p | 82 | -0.7512 | -0.7238 |
| seed_p_vs_seed_pars | 70 | -0.8315 | -0.8621 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
