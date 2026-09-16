# YDR304C
Status: ok. Length: 767 nt. Measured usable bases: 665. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 665 | 0.2975 | 0.2932 |
| rnafold | ok | 665 | 0.3114 | 0.3292 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 615 | -0.1041 | 0.1875 |
| seed_p | 615 | -0.0809 | 0.0858 |
| seed_p_vs_seed_pars | 586 | -0.1876 | -0.0643 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
