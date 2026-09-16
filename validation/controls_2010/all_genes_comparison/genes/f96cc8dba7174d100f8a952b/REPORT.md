# YGR230W
Status: ok. Length: 645 nt. Measured usable bases: 210. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 210 | 0.2910 | 0.2646 |
| rnafold | ok | 210 | 0.3097 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.0993 | 0.2717 |
| seed_p | 45 | -0.4450 | -0.1919 |
| seed_p_vs_seed_pars | 36 | -0.8690 | -0.7563 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
