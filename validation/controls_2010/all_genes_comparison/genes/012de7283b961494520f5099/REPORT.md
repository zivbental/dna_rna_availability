# YJR144W
Status: ok. Length: 901 nt. Measured usable bases: 493. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 493 | 0.3806 | 0.3945 |
| rnafold | ok | 493 | 0.3434 | 0.3524 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | 0.2152 | -0.1164 |
| seed_p | 157 | -0.1199 | -0.1882 |
| seed_p_vs_seed_pars | 125 | -0.5718 | -0.5045 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
