# YGL058W
Status: ok. Length: 800 nt. Measured usable bases: 476. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 476 | 0.2599 | 0.2353 |
| rnafold | ok | 476 | 0.1457 | 0.1501 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 198 | 0.0240 | 0.0462 |
| seed_p | 198 | -0.0961 | -0.0948 |
| seed_p_vs_seed_pars | 164 | -0.2107 | -0.1430 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
