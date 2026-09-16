# YDR331W
Status: ok. Length: 1305 nt. Measured usable bases: 697. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 697 | 0.3094 | 0.3018 |
| rnafold | ok | 697 | 0.2511 | 0.2375 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 160 | -0.0801 | 0.1554 |
| seed_p | 160 | -0.0368 | 0.0361 |
| seed_p_vs_seed_pars | 123 | -0.2965 | -0.2701 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
