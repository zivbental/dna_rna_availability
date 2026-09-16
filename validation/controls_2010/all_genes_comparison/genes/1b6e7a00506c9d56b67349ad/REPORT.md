# YLR204W
Status: ok. Length: 493 nt. Measured usable bases: 191. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 191 | 0.2435 | 0.2532 |
| rnafold | ok | 191 | 0.3315 | 0.3561 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | 0.5270 | 0.6571 |
| seed_p | 36 | 0.1680 | 0.3003 |
| seed_p_vs_seed_pars | 16 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
