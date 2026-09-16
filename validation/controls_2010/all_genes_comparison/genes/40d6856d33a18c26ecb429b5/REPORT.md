# YJR024C
Status: ok. Length: 849 nt. Measured usable bases: 610. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 610 | 0.3561 | 0.3564 |
| rnafold | ok | 610 | 0.3943 | 0.3993 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 454 | -0.1256 | -0.1122 |
| seed_p | 454 | 0.0233 | 0.0188 |
| seed_p_vs_seed_pars | 370 | -0.2612 | -0.2164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
