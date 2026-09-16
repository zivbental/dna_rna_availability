# YJL063C
Status: ok. Length: 806 nt. Measured usable bases: 453. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 453 | 0.3228 | 0.3073 |
| rnafold | ok | 453 | 0.3185 | 0.3066 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 178 | 0.5408 | 0.0957 |
| seed_p | 178 | 0.0067 | -0.1835 |
| seed_p_vs_seed_pars | 135 | -0.3741 | -0.4451 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
