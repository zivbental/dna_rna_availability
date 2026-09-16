# YJR010C-A
Status: ok. Length: 498 nt. Measured usable bases: 279. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 279 | 0.4634 | 0.4417 |
| rnafold | ok | 279 | 0.3911 | 0.3884 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.4224 | -0.1742 |
| seed_p | 149 | -0.0661 | -0.0801 |
| seed_p_vs_seed_pars | 106 | -0.4607 | -0.5010 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
