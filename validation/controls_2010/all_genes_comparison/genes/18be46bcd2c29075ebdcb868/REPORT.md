# YMR178W
Status: ok. Length: 1008 nt. Measured usable bases: 543. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 543 | 0.3554 | 0.3416 |
| rnafold | ok | 543 | 0.3216 | 0.2941 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | -0.0205 | -0.2931 |
| seed_p | 172 | -0.2576 | -0.3542 |
| seed_p_vs_seed_pars | 127 | -0.4961 | -0.5385 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
