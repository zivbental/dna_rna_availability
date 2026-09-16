# YMR264W
Status: ok. Length: 780 nt. Measured usable bases: 549. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 549 | 0.2284 | 0.2115 |
| rnafold | ok | 549 | 0.1976 | 0.1924 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 393 | 0.0784 | 0.0755 |
| seed_p | 393 | -0.1035 | -0.0332 |
| seed_p_vs_seed_pars | 287 | -0.2470 | -0.2226 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
