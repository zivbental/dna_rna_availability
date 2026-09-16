# YKR013W
Status: ok. Length: 1229 nt. Measured usable bases: 1105. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1105 | 0.2367 | 0.2197 |
| rnafold | ok | 1105 | 0.2297 | 0.2186 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1062 | -0.1069 | -0.1906 |
| seed_p | 1062 | -0.2144 | -0.2407 |
| seed_p_vs_seed_pars | 1004 | -0.2565 | -0.2703 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
