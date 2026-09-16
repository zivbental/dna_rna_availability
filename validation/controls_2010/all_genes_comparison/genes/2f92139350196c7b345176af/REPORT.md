# YBR129C
Status: ok. Length: 1136 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.4159 | 0.4040 |
| rnafold | ok | 399 | 0.4009 | 0.3823 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | -0.3761 | -0.5140 |
| seed_p | 59 | -0.4121 | -0.0260 |
| seed_p_vs_seed_pars | 50 | -0.8592 | -0.4479 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
