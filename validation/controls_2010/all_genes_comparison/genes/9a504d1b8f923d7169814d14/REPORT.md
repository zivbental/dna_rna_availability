# YDR003W
Status: ok. Length: 747 nt. Measured usable bases: 299. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 299 | 0.3641 | 0.3373 |
| rnafold | ok | 299 | 0.3495 | 0.3378 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.7569 | 0.8882 |
| seed_p | 34 | 0.1048 | 0.2427 |
| seed_p_vs_seed_pars | 30 | -0.3225 | -0.3585 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
