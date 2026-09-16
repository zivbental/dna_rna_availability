# YGR209C
Status: ok. Length: 413 nt. Measured usable bases: 378. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 378 | 0.3074 | 0.3005 |
| rnafold | ok | 378 | 0.3238 | 0.3180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 372 | -0.0246 | 0.0932 |
| seed_p | 372 | -0.2121 | -0.1660 |
| seed_p_vs_seed_pars | 359 | -0.3832 | -0.3241 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
