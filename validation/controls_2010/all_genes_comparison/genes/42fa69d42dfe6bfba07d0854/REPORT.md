# YKL126W
Status: ok. Length: 2293 nt. Measured usable bases: 1487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1487 | 0.2777 | 0.2643 |
| rnafold | ok | 1487 | 0.2422 | 0.2308 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 649 | -0.0114 | -0.1286 |
| seed_p | 649 | -0.2531 | -0.2251 |
| seed_p_vs_seed_pars | 493 | -0.5019 | -0.3216 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
