# YOR161C
Status: ok. Length: 1620 nt. Measured usable bases: 958. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 958 | 0.2771 | 0.2656 |
| rnafold | ok | 958 | 0.2458 | 0.2443 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 285 | 0.0535 | -0.0539 |
| seed_p | 285 | -0.1692 | -0.2163 |
| seed_p_vs_seed_pars | 210 | -0.1457 | -0.2802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
