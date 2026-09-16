# YGR085C
Status: ok. Length: 618 nt. Measured usable bases: 168. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 168 | 0.4122 | 0.4292 |
| rnafold | ok | 168 | 0.3077 | 0.2650 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | -0.3543 | -0.7613 |
| seed_p | 105 | -0.6015 | -0.6624 |
| seed_p_vs_seed_pars | 75 | -0.4609 | -0.7586 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
