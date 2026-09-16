# YLR262C-A
Status: ok. Length: 290 nt. Measured usable bases: 214. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 214 | 0.2569 | 0.2716 |
| rnafold | ok | 214 | 0.1889 | 0.1912 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.0383 | 0.3223 |
| seed_p | 153 | 0.3256 | 0.1323 |
| seed_p_vs_seed_pars | 142 | 0.2659 | 0.0192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
