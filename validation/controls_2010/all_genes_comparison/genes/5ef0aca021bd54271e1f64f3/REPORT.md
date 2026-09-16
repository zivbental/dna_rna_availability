# YPL178W
Status: ok. Length: 790 nt. Measured usable bases: 527. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 527 | 0.2280 | 0.2107 |
| rnafold | ok | 527 | 0.1744 | 0.1601 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 311 | -0.1979 | -0.2286 |
| seed_p | 311 | -0.2618 | -0.2999 |
| seed_p_vs_seed_pars | 247 | -0.4499 | -0.3461 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
