# YKL027W
Status: ok. Length: 1453 nt. Measured usable bases: 689. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 689 | 0.4230 | 0.4095 |
| rnafold | ok | 689 | 0.3612 | 0.3596 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 76 | 0.0105 | -0.1481 |
| seed_p | 76 | -0.3568 | -0.3315 |
| seed_p_vs_seed_pars | 62 | -0.8186 | -0.7614 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
