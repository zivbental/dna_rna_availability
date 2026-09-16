# YOR369C
Status: ok. Length: 586 nt. Measured usable bases: 553. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 553 | 0.3880 | 0.3605 |
| rnafold | ok | 553 | 0.3421 | 0.3210 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 543 | -0.1056 | 0.0615 |
| seed_p | 543 | -0.1994 | -0.1963 |
| seed_p_vs_seed_pars | 523 | -0.2404 | -0.2693 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
