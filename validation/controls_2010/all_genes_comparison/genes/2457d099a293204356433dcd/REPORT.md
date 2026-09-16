# YMR146C
Status: ok. Length: 1169 nt. Measured usable bases: 950. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 950 | 0.2925 | 0.2822 |
| rnafold | ok | 950 | 0.2532 | 0.2464 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 854 | -0.0840 | -0.0847 |
| seed_p | 854 | -0.2036 | -0.1924 |
| seed_p_vs_seed_pars | 644 | -0.4940 | -0.4411 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
