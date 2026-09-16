# YKL170W
Status: ok. Length: 630 nt. Measured usable bases: 311. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 311 | 0.3002 | 0.2870 |
| rnafold | ok | 311 | 0.3263 | 0.3254 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.1881 | -0.6300 |
| seed_p | 58 | -0.2188 | -0.2840 |
| seed_p_vs_seed_pars | 51 | -0.4524 | -0.3420 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
