# YFL021W
Status: ok. Length: 1679 nt. Measured usable bases: 644. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 644 | 0.2530 | 0.2436 |
| rnafold | ok | 644 | 0.2538 | 0.2446 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.5770 | -0.6755 |
| seed_p | 39 | -0.3064 | -0.0632 |
| seed_p_vs_seed_pars | 21 | -0.9113 | -0.9751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
