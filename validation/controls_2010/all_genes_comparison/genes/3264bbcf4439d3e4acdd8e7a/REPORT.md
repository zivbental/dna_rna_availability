# YPL128C
Status: ok. Length: 1689 nt. Measured usable bases: 915. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 915 | 0.1877 | 0.2048 |
| rnafold | ok | 915 | 0.1970 | 0.2101 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | 0.1692 | -0.0008 |
| seed_p | 203 | -0.0646 | -0.1821 |
| seed_p_vs_seed_pars | 132 | 0.0435 | -0.0640 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
