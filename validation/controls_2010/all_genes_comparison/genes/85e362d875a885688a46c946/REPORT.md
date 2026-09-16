# YDR165W
Status: ok. Length: 1613 nt. Measured usable bases: 902. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 902 | 0.2948 | 0.2818 |
| rnafold | ok | 902 | 0.2279 | 0.2212 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 310 | -0.1656 | -0.1135 |
| seed_p | 310 | 0.0243 | 0.0487 |
| seed_p_vs_seed_pars | 195 | -0.1386 | -0.1044 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
