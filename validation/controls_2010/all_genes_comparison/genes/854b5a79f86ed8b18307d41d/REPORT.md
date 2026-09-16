# YBR195C
Status: ok. Length: 1359 nt. Measured usable bases: 617. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 617 | 0.3606 | 0.3520 |
| rnafold | ok | 617 | 0.3254 | 0.3156 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | -0.5135 | -0.4758 |
| seed_p | 95 | -0.2108 | -0.2626 |
| seed_p_vs_seed_pars | 76 | -0.4482 | -0.6447 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
