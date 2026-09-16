# YMR238W
Status: ok. Length: 1596 nt. Measured usable bases: 949. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 949 | 0.3577 | 0.3352 |
| rnafold | ok | 949 | 0.2766 | 0.2876 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 381 | -0.1102 | -0.1843 |
| seed_p | 381 | -0.2876 | -0.1990 |
| seed_p_vs_seed_pars | 287 | -0.3369 | -0.2301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
