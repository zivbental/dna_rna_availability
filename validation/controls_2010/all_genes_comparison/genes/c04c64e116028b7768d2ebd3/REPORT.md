# YDR538W
Status: ok. Length: 940 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.3005 | 0.3156 |
| rnafold | ok | 454 | 0.2285 | 0.2669 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | 0.1713 | 0.3255 |
| seed_p | 51 | -0.0327 | 0.1746 |
| seed_p_vs_seed_pars | 42 | -0.2665 | -0.0816 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
