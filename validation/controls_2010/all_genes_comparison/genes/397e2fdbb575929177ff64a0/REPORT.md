# YER092W
Status: ok. Length: 378 nt. Measured usable bases: 218. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 218 | 0.2900 | 0.2709 |
| rnafold | ok | 218 | 0.2099 | 0.2350 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.1892 | 0.4381 |
| seed_p | 62 | 0.7264 | 0.6269 |
| seed_p_vs_seed_pars | 42 | 0.6426 | 0.5111 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
