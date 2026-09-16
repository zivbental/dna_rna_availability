# YHR132C
Status: ok. Length: 1479 nt. Measured usable bases: 1043. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1043 | 0.3703 | 0.3563 |
| rnafold | ok | 1043 | 0.2561 | 0.2337 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 698 | -0.0508 | -0.0294 |
| seed_p | 698 | -0.1104 | -0.0897 |
| seed_p_vs_seed_pars | 555 | -0.2869 | -0.2199 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
