# YLL028W
Status: ok. Length: 2062 nt. Measured usable bases: 1075. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1075 | 0.2862 | 0.2710 |
| rnafold | ok | 1075 | 0.2317 | 0.2256 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 270 | 0.0209 | 0.0668 |
| seed_p | 270 | -0.0349 | -0.0634 |
| seed_p_vs_seed_pars | 197 | -0.0700 | -0.0839 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
