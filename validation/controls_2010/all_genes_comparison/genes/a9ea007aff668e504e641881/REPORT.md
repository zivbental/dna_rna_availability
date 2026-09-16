# YPL003W
Status: ok. Length: 1438 nt. Measured usable bases: 559. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 559 | 0.3346 | 0.3230 |
| rnafold | ok | 559 | 0.2465 | 0.2497 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | 0.1787 | 0.2182 |
| seed_p | 37 | 0.0443 | 0.3909 |
| seed_p_vs_seed_pars | 32 | 0.5848 | 0.6938 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
