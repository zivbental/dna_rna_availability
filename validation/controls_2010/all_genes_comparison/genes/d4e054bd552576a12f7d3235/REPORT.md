# YGR158C
Status: ok. Length: 1009 nt. Measured usable bases: 421. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 421 | 0.2670 | 0.2618 |
| rnafold | ok | 421 | 0.2762 | 0.3020 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | 0.2465 | 0.4675 |
| seed_p | 66 | 0.4014 | 0.5256 |
| seed_p_vs_seed_pars | 51 | 0.4599 | 0.3088 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
