# YDR339C
Status: ok. Length: 632 nt. Measured usable bases: 338. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 338 | 0.2624 | 0.2583 |
| rnafold | ok | 338 | 0.1787 | 0.1607 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | 0.1908 | 0.3082 |
| seed_p | 122 | 0.0902 | 0.0519 |
| seed_p_vs_seed_pars | 109 | -0.1958 | -0.1167 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
