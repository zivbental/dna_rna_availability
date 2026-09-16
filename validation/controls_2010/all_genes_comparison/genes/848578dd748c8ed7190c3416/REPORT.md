# YGL105W
Status: ok. Length: 1276 nt. Measured usable bases: 1071. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1071 | 0.2652 | 0.2580 |
| rnafold | ok | 1071 | 0.2321 | 0.2347 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 961 | -0.0225 | -0.1474 |
| seed_p | 961 | -0.0375 | -0.1453 |
| seed_p_vs_seed_pars | 814 | -0.0744 | -0.2080 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
