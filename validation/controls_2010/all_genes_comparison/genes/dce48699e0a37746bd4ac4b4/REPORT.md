# YOL159C
Status: ok. Length: 575 nt. Measured usable bases: 249. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 249 | 0.1734 | 0.1698 |
| rnafold | ok | 249 | 0.1692 | 0.1433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | -0.0429 | 0.2005 |
| seed_p | 31 | -0.0606 | -0.0518 |
| seed_p_vs_seed_pars | 30 | 0.0727 | -0.3858 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
