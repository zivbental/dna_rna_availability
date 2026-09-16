# YMR089C
Status: ok. Length: 2776 nt. Measured usable bases: 1185. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1185 | 0.3155 | 0.3055 |
| rnafold | ok | 1185 | 0.2579 | 0.2636 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 120 | -0.2922 | -0.1714 |
| seed_p | 120 | -0.4601 | -0.3395 |
| seed_p_vs_seed_pars | 71 | -0.7042 | -0.5831 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
