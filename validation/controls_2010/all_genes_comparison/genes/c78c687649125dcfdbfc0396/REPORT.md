# YDL067C
Status: ok. Length: 449 nt. Measured usable bases: 293. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 293 | 0.0917 | 0.0693 |
| rnafold | ok | 293 | 0.1099 | 0.0714 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 182 | 0.2618 | 0.2339 |
| seed_p | 182 | 0.1279 | 0.1074 |
| seed_p_vs_seed_pars | 153 | 0.1932 | 0.2210 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
