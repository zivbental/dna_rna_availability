# YDL133C-A
Status: ok. Length: 280 nt. Measured usable bases: 171. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 171 | 0.2833 | 0.3266 |
| rnafold | ok | 171 | 0.2142 | 0.2576 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.4961 | -0.5371 |
| seed_p | 138 | -0.6399 | -0.6356 |
| seed_p_vs_seed_pars | 138 | -0.4711 | -0.5573 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
