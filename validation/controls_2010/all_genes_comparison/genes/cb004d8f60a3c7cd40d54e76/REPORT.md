# YPL118W
Status: ok. Length: 1222 nt. Measured usable bases: 544. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 544 | 0.2530 | 0.2425 |
| rnafold | ok | 544 | 0.2366 | 0.2188 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.0807 | -0.3915 |
| seed_p | 62 | 0.2676 | -0.0448 |
| seed_p_vs_seed_pars | 40 | 0.1887 | 0.1379 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
