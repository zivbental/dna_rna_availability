# YOR007C
Status: ok. Length: 1154 nt. Measured usable bases: 998. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 998 | 0.4171 | 0.4109 |
| rnafold | ok | 998 | 0.4181 | 0.3981 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 934 | -0.2173 | -0.2245 |
| seed_p | 934 | -0.4581 | -0.3980 |
| seed_p_vs_seed_pars | 777 | -0.4976 | -0.4245 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
