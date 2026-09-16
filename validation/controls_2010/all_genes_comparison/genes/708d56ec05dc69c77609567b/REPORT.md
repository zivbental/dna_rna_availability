# YGL027C
Status: ok. Length: 2619 nt. Measured usable bases: 1430. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1430 | 0.3339 | 0.3187 |
| rnafold | ok | 1430 | 0.2662 | 0.2710 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 344 | -0.1904 | -0.0665 |
| seed_p | 344 | -0.3754 | -0.3227 |
| seed_p_vs_seed_pars | 248 | -0.4720 | -0.5100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
