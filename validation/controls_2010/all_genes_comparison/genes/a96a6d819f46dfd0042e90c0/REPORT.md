# YNL149C
Status: ok. Length: 532 nt. Measured usable bases: 377. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 377 | 0.4108 | 0.4113 |
| rnafold | ok | 377 | 0.3579 | 0.3643 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 260 | -0.2095 | -0.4971 |
| seed_p | 260 | -0.1991 | -0.3918 |
| seed_p_vs_seed_pars | 218 | -0.2138 | -0.4146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
