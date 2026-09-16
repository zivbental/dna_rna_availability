# YER118C
Status: ok. Length: 1455 nt. Measured usable bases: 864. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 864 | 0.1991 | 0.1994 |
| rnafold | ok | 864 | 0.1751 | 0.1591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 312 | 0.0815 | -0.0145 |
| seed_p | 312 | -0.1112 | -0.1702 |
| seed_p_vs_seed_pars | 209 | -0.2375 | -0.1883 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
