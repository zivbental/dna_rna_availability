# YML125C
Status: ok. Length: 1011 nt. Measured usable bases: 869. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 869 | 0.4117 | 0.4059 |
| rnafold | ok | 869 | 0.3981 | 0.3957 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 811 | -0.0193 | -0.1746 |
| seed_p | 811 | -0.2511 | -0.2390 |
| seed_p_vs_seed_pars | 683 | -0.3319 | -0.3146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
