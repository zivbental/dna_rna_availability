# YML029W
Status: ok. Length: 3020 nt. Measured usable bases: 1235. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1235 | 0.3694 | 0.3601 |
| rnafold | ok | 1235 | 0.2853 | 0.2796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.0421 | 0.1104 |
| seed_p | 143 | -0.3015 | -0.2016 |
| seed_p_vs_seed_pars | 97 | 0.0572 | 0.1223 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
