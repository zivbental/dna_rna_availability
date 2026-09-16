# YDR098C
Status: ok. Length: 858 nt. Measured usable bases: 588. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 588 | 0.3511 | 0.3513 |
| rnafold | ok | 588 | 0.2799 | 0.3168 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 374 | -0.0918 | -0.3340 |
| seed_p | 374 | -0.2986 | -0.3790 |
| seed_p_vs_seed_pars | 316 | -0.1554 | -0.1547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
