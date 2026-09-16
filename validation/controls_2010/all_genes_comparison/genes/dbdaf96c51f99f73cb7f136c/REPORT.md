# YDR062W
Status: ok. Length: 2049 nt. Measured usable bases: 1331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1331 | 0.2767 | 0.2587 |
| rnafold | ok | 1331 | 0.2582 | 0.2427 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 686 | -0.1761 | -0.0330 |
| seed_p | 686 | -0.1892 | -0.2452 |
| seed_p_vs_seed_pars | 518 | -0.3158 | -0.2960 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
