# YDR454C
Status: ok. Length: 680 nt. Measured usable bases: 591. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 591 | 0.3558 | 0.3372 |
| rnafold | ok | 591 | 0.2372 | 0.2301 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 561 | -0.1667 | -0.1612 |
| seed_p | 561 | -0.2137 | -0.1795 |
| seed_p_vs_seed_pars | 529 | -0.4208 | -0.3589 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
