# YLL036C
Status: ok. Length: 1594 nt. Measured usable bases: 685. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 685 | 0.3210 | 0.3016 |
| rnafold | ok | 685 | 0.3248 | 0.3152 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | -0.1616 | -0.3759 |
| seed_p | 63 | -0.1622 | -0.0444 |
| seed_p_vs_seed_pars | 58 | -0.0727 | 0.1409 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
