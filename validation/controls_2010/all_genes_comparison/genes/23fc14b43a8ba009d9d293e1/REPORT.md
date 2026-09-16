# YNR003C
Status: ok. Length: 1055 nt. Measured usable bases: 624. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 624 | 0.3707 | 0.3689 |
| rnafold | ok | 624 | 0.3485 | 0.3565 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 182 | -0.4619 | -0.3282 |
| seed_p | 182 | -0.6010 | -0.4623 |
| seed_p_vs_seed_pars | 145 | -0.7207 | -0.6577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
