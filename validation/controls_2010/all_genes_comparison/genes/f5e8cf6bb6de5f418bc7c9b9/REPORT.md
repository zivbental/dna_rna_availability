# YMR067C
Status: ok. Length: 1276 nt. Measured usable bases: 519. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 519 | 0.3537 | 0.3387 |
| rnafold | ok | 519 | 0.3002 | 0.3076 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | 0.1395 | 0.1894 |
| seed_p | 53 | 0.2357 | 0.2325 |
| seed_p_vs_seed_pars | 38 | 0.2880 | 0.3434 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
