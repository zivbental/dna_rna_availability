# YFR014C
Status: ok. Length: 1737 nt. Measured usable bases: 579. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 579 | 0.3425 | 0.3267 |
| rnafold | ok | 579 | 0.2296 | 0.2441 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.2554 | -0.1675 |
| seed_p | 62 | 0.0686 | 0.1020 |
| seed_p_vs_seed_pars | 56 | 0.0482 | -0.1338 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
