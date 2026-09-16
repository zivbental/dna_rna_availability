# YJR005W
Status: ok. Length: 2441 nt. Measured usable bases: 917. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 917 | 0.4008 | 0.3739 |
| rnafold | ok | 917 | 0.3186 | 0.3228 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.1993 | -0.3751 |
| seed_p | 60 | -0.4674 | -0.1443 |
| seed_p_vs_seed_pars | 45 | -0.4976 | -0.3495 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
