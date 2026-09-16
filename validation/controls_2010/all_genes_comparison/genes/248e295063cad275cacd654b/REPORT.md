# YJL118W
Status: ok. Length: 829 nt. Measured usable bases: 382. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 382 | 0.2408 | 0.2196 |
| rnafold | ok | 382 | 0.2101 | 0.2054 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | 0.0435 | -0.2506 |
| seed_p | 94 | -0.0557 | 0.0638 |
| seed_p_vs_seed_pars | 87 | -0.2303 | 0.0126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
