# YIL029C
Status: ok. Length: 889 nt. Measured usable bases: 227. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 227 | 0.3005 | 0.3406 |
| rnafold | ok | 227 | 0.3585 | 0.3919 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.3380 | -0.2695 |
| seed_p | 44 | -0.3321 | -0.6869 |
| seed_p_vs_seed_pars | 44 | -0.4128 | -0.7242 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
