# YDR411C
Status: ok. Length: 1115 nt. Measured usable bases: 698. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 698 | 0.2747 | 0.2690 |
| rnafold | ok | 698 | 0.2265 | 0.2222 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 303 | -0.0298 | -0.1128 |
| seed_p | 303 | -0.0957 | -0.1229 |
| seed_p_vs_seed_pars | 233 | -0.2170 | -0.2921 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
