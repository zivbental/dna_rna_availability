# YGR133W
Status: ok. Length: 804 nt. Measured usable bases: 337. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.2827 | 0.2809 |
| rnafold | ok | 337 | 0.2112 | 0.2186 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.2385 | 0.0084 |
| seed_p | 72 | 0.0668 | 0.0122 |
| seed_p_vs_seed_pars | 67 | -0.3017 | -0.3594 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
