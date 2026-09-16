# YHR215W
Status: ok. Length: 1516 nt. Measured usable bases: 135. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 135 | 0.2121 | 0.1753 |
| rnafold | ok | 135 | 0.1950 | 0.2168 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.1799 | -0.4123 |
| seed_p | 44 | -0.3472 | -0.3569 |
| seed_p_vs_seed_pars | 41 | 0.7629 | 0.3581 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
