# YIL070C
Status: ok. Length: 937 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.2917 | 0.2860 |
| rnafold | ok | 402 | 0.2320 | 0.2296 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | 0.0345 | 0.3266 |
| seed_p | 35 | 0.0647 | 0.1511 |
| seed_p_vs_seed_pars | 29 | 0.5553 | 0.4897 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
