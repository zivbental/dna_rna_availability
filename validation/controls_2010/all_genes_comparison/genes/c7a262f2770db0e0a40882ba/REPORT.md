# YCL037C
Status: ok. Length: 1522 nt. Measured usable bases: 712. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 712 | 0.2276 | 0.2054 |
| rnafold | ok | 712 | 0.1899 | 0.1675 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | 0.2618 | 0.2585 |
| seed_p | 88 | -0.1901 | -0.0121 |
| seed_p_vs_seed_pars | 50 | -0.1940 | -0.1281 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
