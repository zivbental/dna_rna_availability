# YKL152C
Status: ok. Length: 872 nt. Measured usable bases: 837. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 837 | 0.3714 | 0.3552 |
| rnafold | ok | 837 | 0.2579 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 820 | -0.1651 | -0.2021 |
| seed_p | 820 | -0.3283 | -0.3383 |
| seed_p_vs_seed_pars | 818 | -0.3977 | -0.4564 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
