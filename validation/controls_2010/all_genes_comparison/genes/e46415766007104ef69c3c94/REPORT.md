# YER089C
Status: ok. Length: 1754 nt. Measured usable bases: 1048. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1048 | 0.3076 | 0.2847 |
| rnafold | ok | 1048 | 0.2839 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 509 | -0.1244 | 0.0212 |
| seed_p | 509 | -0.2215 | -0.1279 |
| seed_p_vs_seed_pars | 359 | -0.4199 | -0.2992 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
