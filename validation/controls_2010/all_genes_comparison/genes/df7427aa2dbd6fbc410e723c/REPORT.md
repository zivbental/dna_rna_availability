# YKL116C
Status: ok. Length: 1983 nt. Measured usable bases: 930. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 930 | 0.2956 | 0.2990 |
| rnafold | ok | 930 | 0.2519 | 0.2510 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | -0.4874 | -0.5907 |
| seed_p | 124 | -0.3775 | -0.4630 |
| seed_p_vs_seed_pars | 75 | -0.3362 | -0.2641 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
