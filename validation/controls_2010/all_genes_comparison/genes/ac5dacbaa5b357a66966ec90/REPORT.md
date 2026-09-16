# YHR106W
Status: ok. Length: 1332 nt. Measured usable bases: 479. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 479 | 0.4645 | 0.4436 |
| rnafold | ok | 479 | 0.3734 | 0.3407 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 20 | 0.4986 | 0.6569 |
| seed_p | 20 | 0.5958 | 0.4659 |
| seed_p_vs_seed_pars | 6 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
