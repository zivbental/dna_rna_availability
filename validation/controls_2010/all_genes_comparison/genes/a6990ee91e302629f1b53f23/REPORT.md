# YDR234W
Status: ok. Length: 2451 nt. Measured usable bases: 1562. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1562 | 0.3091 | 0.2818 |
| rnafold | ok | 1562 | 0.2841 | 0.2498 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 891 | 0.0912 | 0.0261 |
| seed_p | 891 | -0.0787 | -0.0456 |
| seed_p_vs_seed_pars | 625 | -0.2112 | -0.0730 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
