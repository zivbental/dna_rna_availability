# YGR060W
Status: ok. Length: 1051 nt. Measured usable bases: 917. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 917 | 0.1877 | 0.1768 |
| rnafold | ok | 917 | 0.1889 | 0.1859 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 929 | -0.0241 | 0.0554 |
| seed_p | 929 | -0.0621 | -0.0218 |
| seed_p_vs_seed_pars | 818 | -0.0716 | -0.0282 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
