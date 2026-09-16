# YOL049W
Status: ok. Length: 1631 nt. Measured usable bases: 1001. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1001 | 0.3548 | 0.3411 |
| rnafold | ok | 1001 | 0.3683 | 0.3563 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 375 | -0.1661 | -0.2902 |
| seed_p | 375 | -0.1971 | -0.1712 |
| seed_p_vs_seed_pars | 274 | -0.2693 | -0.3135 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
