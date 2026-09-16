# YLR401C
Status: ok. Length: 2073 nt. Measured usable bases: 947. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 947 | 0.3902 | 0.3832 |
| rnafold | ok | 947 | 0.4036 | 0.3910 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 177 | -0.0560 | 0.1900 |
| seed_p | 177 | 0.1136 | 0.1075 |
| seed_p_vs_seed_pars | 140 | -0.4243 | -0.2871 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
