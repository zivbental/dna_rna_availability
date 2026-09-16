# YDR266C
Status: ok. Length: 2235 nt. Measured usable bases: 976. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 976 | 0.3200 | 0.3134 |
| rnafold | ok | 976 | 0.3054 | 0.3217 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.0186 | 0.1109 |
| seed_p | 121 | -0.3262 | -0.3065 |
| seed_p_vs_seed_pars | 75 | -0.5034 | -0.4789 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
