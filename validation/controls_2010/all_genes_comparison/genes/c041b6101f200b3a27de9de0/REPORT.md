# YGL043W
Status: ok. Length: 1184 nt. Measured usable bases: 774. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 774 | 0.3029 | 0.2892 |
| rnafold | ok | 774 | 0.2880 | 0.2744 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 453 | -0.0021 | -0.0056 |
| seed_p | 453 | -0.0873 | -0.0051 |
| seed_p_vs_seed_pars | 329 | -0.2381 | -0.1332 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
