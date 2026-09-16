# YGL252C
Status: ok. Length: 2008 nt. Measured usable bases: 839. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 839 | 0.3414 | 0.3293 |
| rnafold | ok | 839 | 0.2980 | 0.2777 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | -0.3820 | -0.6038 |
| seed_p | 85 | -0.6523 | -0.6662 |
| seed_p_vs_seed_pars | 67 | -0.2188 | -0.2201 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
