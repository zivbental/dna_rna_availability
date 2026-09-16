# YEL001C
Status: ok. Length: 783 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.3895 | 0.3694 |
| rnafold | ok | 633 | 0.3654 | 0.3541 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 581 | -0.1505 | -0.2198 |
| seed_p | 581 | -0.4369 | -0.3099 |
| seed_p_vs_seed_pars | 475 | -0.5116 | -0.3860 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
