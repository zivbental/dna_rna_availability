# YKR001C
Status: ok. Length: 2269 nt. Measured usable bases: 1534. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1534 | 0.3010 | 0.2997 |
| rnafold | ok | 1534 | 0.2134 | 0.2200 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 813 | -0.0888 | -0.2560 |
| seed_p | 813 | -0.1996 | -0.2586 |
| seed_p_vs_seed_pars | 623 | -0.1950 | -0.2809 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
