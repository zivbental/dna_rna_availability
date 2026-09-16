# YMR121C
Status: ok. Length: 747 nt. Measured usable bases: 234. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 234 | 0.4148 | 0.4065 |
| rnafold | ok | 234 | 0.4516 | 0.4564 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 22 | -0.0362 | -0.0990 |
| seed_p | 22 | -0.7372 | -0.6031 |
| seed_p_vs_seed_pars | 13 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
