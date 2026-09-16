# YDR373W
Status: ok. Length: 728 nt. Measured usable bases: 346. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 346 | 0.3120 | 0.3095 |
| rnafold | ok | 346 | 0.2517 | 0.2790 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.1566 | -0.2456 |
| seed_p | 73 | 0.0336 | 0.1756 |
| seed_p_vs_seed_pars | 65 | -0.8211 | -0.4104 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
