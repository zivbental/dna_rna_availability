# RDN5-3
Status: ok. Length: 119 nt. Measured usable bases: 95.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 95 | 0.3104 | 0.2919 |
| rnafold | ok | 95 | 0.3104 | 0.2919 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 80 | 0.3871 | 0.4755 |
| seed_p | 80 | -0.0025 | 0.2507 |
| seed_p_vs_seed_pars | 80 | -0.4858 | -0.3331 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
