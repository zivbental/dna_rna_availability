# YDR206W
Status: ok. Length: 3023 nt. Measured usable bases: 1478. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1478 | 0.3457 | 0.3218 |
| rnafold | ok | 1478 | 0.2968 | 0.2956 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | -0.1952 | -0.2446 |
| seed_p | 246 | -0.1749 | -0.0633 |
| seed_p_vs_seed_pars | 167 | -0.4430 | -0.1625 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
