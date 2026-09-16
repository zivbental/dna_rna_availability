# YLR146C
Status: ok. Length: 996 nt. Measured usable bases: 612. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.3054 | 0.2886 |
| rnafold | ok | 612 | 0.3079 | 0.3190 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 325 | -0.0648 | -0.1338 |
| seed_p | 325 | -0.1693 | -0.0984 |
| seed_p_vs_seed_pars | 251 | -0.3394 | -0.2202 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
