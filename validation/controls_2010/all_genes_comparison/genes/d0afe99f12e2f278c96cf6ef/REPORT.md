# YKL127W
Status: ok. Length: 1877 nt. Measured usable bases: 1263. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1263 | 0.3159 | 0.2958 |
| rnafold | ok | 1263 | 0.2236 | 0.2113 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 729 | -0.3362 | -0.0069 |
| seed_p | 729 | -0.1940 | -0.1155 |
| seed_p_vs_seed_pars | 591 | -0.3284 | -0.2257 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
