# YMR027W
Status: ok. Length: 1527 nt. Measured usable bases: 991. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 991 | 0.3214 | 0.2982 |
| rnafold | ok | 991 | 0.3054 | 0.3000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 499 | -0.0519 | -0.0821 |
| seed_p | 499 | -0.0698 | -0.1365 |
| seed_p_vs_seed_pars | 322 | -0.1780 | -0.3001 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
