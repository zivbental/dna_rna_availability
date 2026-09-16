# YOL146W
Status: ok. Length: 670 nt. Measured usable bases: 333. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 333 | 0.3727 | 0.3644 |
| rnafold | ok | 333 | 0.2373 | 0.2379 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | 0.1900 | 0.1548 |
| seed_p | 86 | 0.5038 | 0.4571 |
| seed_p_vs_seed_pars | 71 | 0.3346 | 0.3088 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
