# YJL039C
Status: ok. Length: 5248 nt. Measured usable bases: 2151. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2151 | 0.3233 | 0.2932 |
| rnafold | ok | 2151 | 0.2539 | 0.2433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | -0.2753 | -0.3045 |
| seed_p | 167 | -0.1597 | -0.1178 |
| seed_p_vs_seed_pars | 78 | -0.1914 | -0.2109 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
