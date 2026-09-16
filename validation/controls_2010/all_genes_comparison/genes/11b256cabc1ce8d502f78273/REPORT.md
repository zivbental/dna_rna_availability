# YOR057W
Status: ok. Length: 1526 nt. Measured usable bases: 528. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 528 | 0.3604 | 0.3595 |
| rnafold | ok | 528 | 0.2358 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | -0.5225 | -0.5224 |
| seed_p | 31 | -0.1864 | -0.4094 |
| seed_p_vs_seed_pars | 9 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
