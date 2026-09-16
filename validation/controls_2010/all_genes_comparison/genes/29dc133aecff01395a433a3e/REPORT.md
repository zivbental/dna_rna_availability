# YER017C
Status: ok. Length: 2423 nt. Measured usable bases: 1031. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1031 | 0.3539 | 0.3403 |
| rnafold | ok | 1031 | 0.3061 | 0.3039 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | -0.0098 | -0.0211 |
| seed_p | 105 | 0.0989 | -0.0810 |
| seed_p_vs_seed_pars | 74 | -0.3630 | -0.3568 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
