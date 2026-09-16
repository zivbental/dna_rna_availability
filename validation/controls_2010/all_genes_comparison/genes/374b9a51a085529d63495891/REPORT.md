# YKL029C
Status: ok. Length: 2055 nt. Measured usable bases: 1377. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1377 | 0.3379 | 0.3023 |
| rnafold | ok | 1377 | 0.2963 | 0.2615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 722 | 0.0283 | -0.1014 |
| seed_p | 722 | -0.1744 | -0.1804 |
| seed_p_vs_seed_pars | 581 | -0.0926 | -0.0627 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
