# YBR135W
Status: ok. Length: 658 nt. Measured usable bases: 405. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 405 | 0.3203 | 0.3203 |
| rnafold | ok | 405 | 0.2438 | 0.2613 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 195 | -0.0272 | 0.1095 |
| seed_p | 195 | 0.1801 | 0.1809 |
| seed_p_vs_seed_pars | 133 | 0.1133 | 0.1413 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
