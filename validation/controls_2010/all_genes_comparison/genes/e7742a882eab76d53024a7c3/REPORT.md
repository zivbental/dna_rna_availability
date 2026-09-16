# YJR139C
Status: ok. Length: 1208 nt. Measured usable bases: 1006. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1006 | 0.3849 | 0.3714 |
| rnafold | ok | 1006 | 0.3610 | 0.3518 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 930 | -0.1609 | -0.2214 |
| seed_p | 930 | -0.2207 | -0.2358 |
| seed_p_vs_seed_pars | 873 | -0.2951 | -0.3218 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
