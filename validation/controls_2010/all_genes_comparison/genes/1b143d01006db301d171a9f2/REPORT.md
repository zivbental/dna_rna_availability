# YNL094W
Status: ok. Length: 2085 nt. Measured usable bases: 972. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 972 | 0.2548 | 0.2421 |
| rnafold | ok | 972 | 0.1237 | 0.1301 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.0762 | -0.2384 |
| seed_p | 109 | -0.3135 | -0.3131 |
| seed_p_vs_seed_pars | 71 | -0.6410 | -0.6809 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
