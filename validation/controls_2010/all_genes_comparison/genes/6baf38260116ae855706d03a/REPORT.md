# YDL140C
Status: ok. Length: 5350 nt. Measured usable bases: 3016. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3016 | 0.2190 | 0.2149 |
| rnafold | ok | 3016 | 0.2021 | 0.2081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 902 | 0.1773 | -0.0080 |
| seed_p | 902 | 0.1005 | 0.0548 |
| seed_p_vs_seed_pars | 673 | -0.0040 | -0.1284 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
