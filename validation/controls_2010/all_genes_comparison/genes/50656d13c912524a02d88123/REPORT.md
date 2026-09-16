# YPL004C
Status: ok. Length: 1244 nt. Measured usable bases: 1015. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1015 | 0.2996 | 0.2918 |
| rnafold | ok | 1015 | 0.1766 | 0.1871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 872 | 0.0621 | -0.1271 |
| seed_p | 872 | -0.0387 | -0.0485 |
| seed_p_vs_seed_pars | 724 | -0.2203 | -0.2110 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
