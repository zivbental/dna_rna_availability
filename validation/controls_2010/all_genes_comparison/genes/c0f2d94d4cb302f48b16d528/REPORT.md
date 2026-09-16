# YJR141W
Status: ok. Length: 1189 nt. Measured usable bases: 418. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.4712 | 0.4588 |
| rnafold | ok | 418 | 0.3580 | 0.3642 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | -0.1870 | -0.2051 |
| seed_p | 28 | -0.8018 | -0.6962 |
| seed_p_vs_seed_pars | 26 | -0.4889 | -0.2527 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
