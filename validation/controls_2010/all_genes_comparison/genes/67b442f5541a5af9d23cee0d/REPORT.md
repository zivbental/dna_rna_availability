# YDR377W
Status: ok. Length: 787 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.2468 | 0.2326 |
| rnafold | ok | 454 | 0.2637 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 325 | -0.1037 | -0.2753 |
| seed_p | 325 | -0.3633 | -0.3833 |
| seed_p_vs_seed_pars | 239 | -0.3279 | -0.3145 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
