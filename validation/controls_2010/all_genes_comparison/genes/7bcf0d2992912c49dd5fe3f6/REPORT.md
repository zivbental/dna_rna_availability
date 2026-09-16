# YNL256W
Status: ok. Length: 2620 nt. Measured usable bases: 1036. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1036 | 0.3016 | 0.2848 |
| rnafold | ok | 1036 | 0.2856 | 0.2645 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.2134 | 0.3721 |
| seed_p | 79 | 0.4602 | 0.5066 |
| seed_p_vs_seed_pars | 50 | 0.3651 | 0.5576 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
