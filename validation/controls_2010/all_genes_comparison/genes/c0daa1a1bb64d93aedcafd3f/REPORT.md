# YHR034C
Status: ok. Length: 1181 nt. Measured usable bases: 420. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 420 | 0.4481 | 0.4606 |
| rnafold | ok | 420 | 0.3698 | 0.3642 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 29 | -0.1051 | 0.2316 |
| seed_p | 29 | -0.3237 | -0.4283 |
| seed_p_vs_seed_pars | 29 | -0.2730 | -0.4120 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
