# YLR405W
Status: ok. Length: 1253 nt. Measured usable bases: 524. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 524 | 0.3830 | 0.3830 |
| rnafold | ok | 524 | 0.3565 | 0.3724 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.1644 | -0.3073 |
| seed_p | 51 | -0.1991 | -0.0803 |
| seed_p_vs_seed_pars | 29 | 0.5868 | 0.4450 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
