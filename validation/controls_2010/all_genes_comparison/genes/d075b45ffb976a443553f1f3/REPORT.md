# YCR083W
Status: ok. Length: 526 nt. Measured usable bases: 240. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 240 | 0.2980 | 0.3107 |
| rnafold | ok | 240 | 0.3497 | 0.3236 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | 0.3030 | 0.3315 |
| seed_p | 92 | 0.6493 | 0.6602 |
| seed_p_vs_seed_pars | 67 | 0.5874 | 0.7153 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
