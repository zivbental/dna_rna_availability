# YHR094C
Status: ok. Length: 1853 nt. Measured usable bases: 1269. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1269 | 0.2516 | 0.2223 |
| rnafold | ok | 1269 | 0.2215 | 0.1832 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 909 | -0.0783 | 0.0656 |
| seed_p | 909 | -0.1708 | -0.0599 |
| seed_p_vs_seed_pars | 672 | -0.3650 | -0.2284 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
