# YLR138W
Status: ok. Length: 3174 nt. Measured usable bases: 1262. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1262 | 0.3558 | 0.3419 |
| rnafold | ok | 1262 | 0.2260 | 0.2198 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 119 | -0.1856 | -0.4521 |
| seed_p | 119 | -0.0836 | -0.1650 |
| seed_p_vs_seed_pars | 70 | -0.2973 | -0.5817 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
