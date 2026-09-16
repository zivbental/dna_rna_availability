# YOR383C
Status: ok. Length: 781 nt. Measured usable bases: 536. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 536 | 0.0959 | 0.0979 |
| rnafold | ok | 536 | 0.0738 | 0.0820 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 310 | -0.0641 | -0.0444 |
| seed_p | 310 | -0.0299 | -0.1310 |
| seed_p_vs_seed_pars | 246 | -0.2034 | -0.2679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
