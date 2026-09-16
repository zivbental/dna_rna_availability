# YER146W
Status: ok. Length: 367 nt. Measured usable bases: 258. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 258 | 0.4765 | 0.4319 |
| rnafold | ok | 258 | 0.4963 | 0.4317 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 237 | 0.0178 | -0.3059 |
| seed_p | 237 | -0.4116 | -0.5620 |
| seed_p_vs_seed_pars | 206 | -0.7236 | -0.7144 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
