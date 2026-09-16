# YIL040W
Status: ok. Length: 501 nt. Measured usable bases: 271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.2806 | 0.2557 |
| rnafold | ok | 271 | 0.2442 | 0.2570 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | -0.0467 | -0.5045 |
| seed_p | 99 | -0.1529 | -0.5050 |
| seed_p_vs_seed_pars | 56 | 0.5279 | 0.6057 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
