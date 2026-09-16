# YOL060C
Status: ok. Length: 2478 nt. Measured usable bases: 1105. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1105 | 0.2343 | 0.2101 |
| rnafold | ok | 1105 | 0.1918 | 0.1906 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | 0.0450 | 0.0208 |
| seed_p | 118 | -0.3669 | -0.3757 |
| seed_p_vs_seed_pars | 76 | -0.5448 | -0.6576 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
