# YEL026W
Status: ok. Length: 558 nt. Measured usable bases: 464. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 464 | 0.2879 | 0.2950 |
| rnafold | ok | 464 | 0.3220 | 0.3240 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 443 | -0.2113 | -0.2124 |
| seed_p | 443 | -0.3000 | -0.3491 |
| seed_p_vs_seed_pars | 421 | -0.4153 | -0.5249 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
