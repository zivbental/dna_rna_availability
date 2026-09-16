# YEL020W-A
Status: ok. Length: 381 nt. Measured usable bases: 261. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 261 | 0.2821 | 0.2679 |
| rnafold | ok | 261 | 0.3113 | 0.3087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 198 | 0.1124 | -0.2053 |
| seed_p | 198 | 0.0912 | -0.1141 |
| seed_p_vs_seed_pars | 191 | -0.1901 | -0.2231 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
