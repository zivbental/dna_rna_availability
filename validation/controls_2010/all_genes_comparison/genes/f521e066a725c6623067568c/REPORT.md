# YLR332W
Status: ok. Length: 1745 nt. Measured usable bases: 809. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 809 | 0.2722 | 0.2650 |
| rnafold | ok | 809 | 0.1419 | 0.1416 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 148 | -0.5476 | -0.6185 |
| seed_p | 148 | -0.2988 | -0.3037 |
| seed_p_vs_seed_pars | 131 | -0.5668 | -0.3771 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
