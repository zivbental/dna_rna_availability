# YJL014W
Status: ok. Length: 1759 nt. Measured usable bases: 1267. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1267 | 0.3220 | 0.3165 |
| rnafold | ok | 1267 | 0.2817 | 0.2727 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 797 | 0.0171 | -0.1371 |
| seed_p | 797 | -0.1103 | -0.1252 |
| seed_p_vs_seed_pars | 608 | -0.2165 | -0.2010 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
