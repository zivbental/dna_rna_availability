# YGR210C
Status: ok. Length: 1429 nt. Measured usable bases: 945. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 945 | 0.3288 | 0.3253 |
| rnafold | ok | 945 | 0.3246 | 0.3145 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 501 | -0.1024 | -0.1173 |
| seed_p | 501 | -0.1930 | -0.0932 |
| seed_p_vs_seed_pars | 384 | -0.3583 | -0.2217 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
