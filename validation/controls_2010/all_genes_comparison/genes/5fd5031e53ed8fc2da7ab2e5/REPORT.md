# YLR038C
Status: ok. Length: 622 nt. Measured usable bases: 331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 331 | 0.3022 | 0.2890 |
| rnafold | ok | 331 | 0.2062 | 0.1977 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 139 | -0.0037 | -0.0097 |
| seed_p | 139 | -0.3453 | -0.2357 |
| seed_p_vs_seed_pars | 98 | -0.6680 | -0.6103 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
