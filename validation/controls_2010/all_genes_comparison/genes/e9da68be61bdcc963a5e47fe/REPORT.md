# YJR010W
Status: ok. Length: 1777 nt. Measured usable bases: 697. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 697 | 0.2077 | 0.2073 |
| rnafold | ok | 697 | 0.1359 | 0.1565 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | 0.2666 | 0.1874 |
| seed_p | 60 | 0.0524 | 0.1476 |
| seed_p_vs_seed_pars | 54 | 0.2219 | 0.1567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
