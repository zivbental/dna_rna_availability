# YDL054C
Status: ok. Length: 1618 nt. Measured usable bases: 671. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 671 | 0.3341 | 0.3242 |
| rnafold | ok | 671 | 0.3156 | 0.3227 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.5004 | -0.1153 |
| seed_p | 67 | -0.2533 | 0.0496 |
| seed_p_vs_seed_pars | 49 | 0.0194 | 0.1684 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
