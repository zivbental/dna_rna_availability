# YKL205W
Status: ok. Length: 3536 nt. Measured usable bases: 1225. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1225 | 0.2424 | 0.2291 |
| rnafold | ok | 1225 | 0.1839 | 0.1730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.3494 | 0.3706 |
| seed_p | 87 | -0.1426 | -0.0994 |
| seed_p_vs_seed_pars | 76 | -0.0056 | 0.1153 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
