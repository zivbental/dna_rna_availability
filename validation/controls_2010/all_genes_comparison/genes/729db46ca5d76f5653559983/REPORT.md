# YAL032C
Status: ok. Length: 1209 nt. Measured usable bases: 448. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.4062 | 0.3981 |
| rnafold | ok | 448 | 0.3393 | 0.3465 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.1362 | -0.5122 |
| seed_p | 37 | -0.7335 | -0.6586 |
| seed_p_vs_seed_pars | 20 | 0.3259 | 0.1954 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
