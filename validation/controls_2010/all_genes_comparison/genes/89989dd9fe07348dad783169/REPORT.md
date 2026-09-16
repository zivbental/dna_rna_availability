# YGR206W
Status: ok. Length: 428 nt. Measured usable bases: 171. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 171 | 0.4102 | 0.3911 |
| rnafold | ok | 171 | 0.3349 | 0.3455 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.1787 | 0.5391 |
| seed_p | 64 | -0.3595 | -0.2122 |
| seed_p_vs_seed_pars | 59 | -0.1275 | -0.0183 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
