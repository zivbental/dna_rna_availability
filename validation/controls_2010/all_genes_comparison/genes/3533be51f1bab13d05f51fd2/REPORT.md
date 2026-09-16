# YOR126C
Status: ok. Length: 834 nt. Measured usable bases: 344. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 344 | 0.3072 | 0.2997 |
| rnafold | ok | 344 | 0.2969 | 0.2902 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 41 | 0.4084 | 0.5945 |
| seed_p | 41 | 0.1233 | 0.3808 |
| seed_p_vs_seed_pars | 22 | -0.2050 | 0.2880 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
