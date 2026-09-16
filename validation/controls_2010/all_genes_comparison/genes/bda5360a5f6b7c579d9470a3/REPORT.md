# YFR055W
Status: ok. Length: 1493 nt. Measured usable bases: 888. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 888 | 0.3694 | 0.3421 |
| rnafold | ok | 888 | 0.3182 | 0.3241 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 393 | -0.0040 | -0.1281 |
| seed_p | 393 | -0.0285 | -0.1304 |
| seed_p_vs_seed_pars | 291 | -0.1870 | -0.2115 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
