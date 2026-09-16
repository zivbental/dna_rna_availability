# YDR465C
Status: ok. Length: 1420 nt. Measured usable bases: 767. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 767 | 0.3012 | 0.2855 |
| rnafold | ok | 767 | 0.2377 | 0.2419 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | 0.0121 | -0.0613 |
| seed_p | 166 | 0.1083 | 0.1292 |
| seed_p_vs_seed_pars | 126 | -0.3150 | -0.2468 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
