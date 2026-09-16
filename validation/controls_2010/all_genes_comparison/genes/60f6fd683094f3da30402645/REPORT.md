# YMR222C
Status: ok. Length: 745 nt. Measured usable bases: 474. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 474 | 0.3521 | 0.3473 |
| rnafold | ok | 474 | 0.2596 | 0.2760 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 256 | -0.1759 | -0.3832 |
| seed_p | 256 | -0.3410 | -0.3514 |
| seed_p_vs_seed_pars | 220 | -0.4526 | -0.4642 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
