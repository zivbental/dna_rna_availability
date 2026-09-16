# YNL323W
Status: ok. Length: 1441 nt. Measured usable bases: 647. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 647 | 0.4066 | 0.3894 |
| rnafold | ok | 647 | 0.3114 | 0.3071 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 103 | -0.6205 | -0.7423 |
| seed_p | 103 | -0.3608 | -0.3719 |
| seed_p_vs_seed_pars | 85 | -0.3887 | -0.4027 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
