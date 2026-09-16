# YGL202W
Status: ok. Length: 1691 nt. Measured usable bases: 1430. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1430 | 0.2954 | 0.2899 |
| rnafold | ok | 1430 | 0.2459 | 0.2365 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1320 | 0.0090 | -0.0749 |
| seed_p | 1320 | -0.1379 | -0.1524 |
| seed_p_vs_seed_pars | 1162 | -0.1636 | -0.1990 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
