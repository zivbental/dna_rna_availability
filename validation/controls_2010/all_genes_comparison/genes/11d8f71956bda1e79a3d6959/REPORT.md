# YKL146W
Status: ok. Length: 2183 nt. Measured usable bases: 1220. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1220 | 0.3465 | 0.3437 |
| rnafold | ok | 1220 | 0.2553 | 0.2480 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 388 | -0.1135 | -0.1161 |
| seed_p | 388 | -0.3691 | -0.3590 |
| seed_p_vs_seed_pars | 305 | -0.5004 | -0.4892 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
