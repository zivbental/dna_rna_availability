# YKL216W
Status: ok. Length: 1216 nt. Measured usable bases: 821. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 821 | 0.3331 | 0.3228 |
| rnafold | ok | 821 | 0.3068 | 0.3124 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 535 | -0.0125 | 0.0056 |
| seed_p | 535 | -0.0754 | -0.1834 |
| seed_p_vs_seed_pars | 404 | -0.2035 | -0.2650 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
