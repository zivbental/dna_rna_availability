# YBR254C
Status: ok. Length: 672 nt. Measured usable bases: 282. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.2357 | 0.2175 |
| rnafold | ok | 282 | 0.2509 | 0.2567 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | -0.3654 | -0.1904 |
| seed_p | 59 | 0.1762 | -0.0859 |
| seed_p_vs_seed_pars | 36 | 0.7457 | 0.4649 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
