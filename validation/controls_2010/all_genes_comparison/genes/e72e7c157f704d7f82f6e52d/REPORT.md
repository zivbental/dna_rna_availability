# YIL124W
Status: ok. Length: 1044 nt. Measured usable bases: 763. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 763 | 0.4375 | 0.4449 |
| rnafold | ok | 763 | 0.3935 | 0.4168 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 553 | 0.0214 | -0.0574 |
| seed_p | 553 | 0.0016 | 0.0560 |
| seed_p_vs_seed_pars | 439 | -0.1116 | 0.0187 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
