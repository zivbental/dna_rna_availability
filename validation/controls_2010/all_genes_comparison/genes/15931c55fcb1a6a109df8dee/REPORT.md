# YMR173W
Status: ok. Length: 1405 nt. Measured usable bases: 391. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 391 | 0.4379 | 0.4570 |
| rnafold | ok | 391 | 0.3773 | 0.3948 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.1955 | -0.2827 |
| seed_p | 69 | -0.1022 | -0.1941 |
| seed_p_vs_seed_pars | 61 | -0.6077 | -0.6047 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
