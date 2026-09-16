# YDR063W
Status: ok. Length: 633 nt. Measured usable bases: 343. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 343 | 0.2173 | 0.2129 |
| rnafold | ok | 343 | 0.3343 | 0.3432 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 147 | -0.1324 | 0.1229 |
| seed_p | 147 | -0.2032 | -0.0912 |
| seed_p_vs_seed_pars | 121 | -0.4862 | -0.4247 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
