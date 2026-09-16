# YHL032C
Status: ok. Length: 2195 nt. Measured usable bases: 1029. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1029 | 0.3252 | 0.3008 |
| rnafold | ok | 1029 | 0.2087 | 0.2274 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | 0.0420 | 0.0415 |
| seed_p | 88 | -0.0018 | -0.1316 |
| seed_p_vs_seed_pars | 52 | -0.0891 | -0.1369 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
