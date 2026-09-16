# YBR234C
Status: ok. Length: 1247 nt. Measured usable bases: 878. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 878 | 0.3647 | 0.3308 |
| rnafold | ok | 878 | 0.3302 | 0.2991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 616 | 0.1357 | 0.0369 |
| seed_p | 616 | -0.1889 | -0.0989 |
| seed_p_vs_seed_pars | 493 | -0.2660 | -0.2040 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
