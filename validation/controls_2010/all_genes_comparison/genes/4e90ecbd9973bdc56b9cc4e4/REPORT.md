# YML070W
Status: ok. Length: 1881 nt. Measured usable bases: 1254. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1254 | 0.3078 | 0.2736 |
| rnafold | ok | 1254 | 0.2611 | 0.2354 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 737 | -0.1646 | -0.2165 |
| seed_p | 737 | -0.1874 | -0.2068 |
| seed_p_vs_seed_pars | 546 | -0.3095 | -0.3823 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
