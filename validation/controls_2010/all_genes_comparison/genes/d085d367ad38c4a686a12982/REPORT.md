# YFL005W
Status: ok. Length: 1028 nt. Measured usable bases: 721. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 721 | 0.4269 | 0.4225 |
| rnafold | ok | 721 | 0.3320 | 0.3294 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 498 | -0.3260 | -0.3020 |
| seed_p | 498 | -0.3783 | -0.3119 |
| seed_p_vs_seed_pars | 414 | -0.5413 | -0.4888 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
