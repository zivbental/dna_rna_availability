# YJL060W
Status: ok. Length: 1486 nt. Measured usable bases: 752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 752 | 0.3166 | 0.3052 |
| rnafold | ok | 752 | 0.2530 | 0.2448 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 202 | -0.3217 | -0.2007 |
| seed_p | 202 | -0.5353 | -0.5664 |
| seed_p_vs_seed_pars | 155 | -0.4582 | -0.4683 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
