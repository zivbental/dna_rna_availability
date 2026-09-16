# YLR197W
Status: ok. Length: 1741 nt. Measured usable bases: 1273. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1273 | 0.3011 | 0.3086 |
| rnafold | ok | 1273 | 0.2624 | 0.2813 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1019 | -0.1001 | -0.1136 |
| seed_p | 1019 | -0.0251 | -0.0556 |
| seed_p_vs_seed_pars | 872 | -0.1844 | -0.1245 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
