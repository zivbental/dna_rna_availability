# YLR403W
Status: ok. Length: 2437 nt. Measured usable bases: 1185. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1185 | 0.3020 | 0.2849 |
| rnafold | ok | 1185 | 0.2399 | 0.2240 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 218 | 0.3821 | 0.4436 |
| seed_p | 218 | -0.1035 | -0.1246 |
| seed_p_vs_seed_pars | 144 | -0.1886 | -0.1235 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
