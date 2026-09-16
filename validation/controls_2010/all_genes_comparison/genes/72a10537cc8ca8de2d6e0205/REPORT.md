# YHR181W
Status: ok. Length: 835 nt. Measured usable bases: 569. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 569 | 0.2365 | 0.2252 |
| rnafold | ok | 569 | 0.1692 | 0.1581 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 364 | -0.1339 | -0.0135 |
| seed_p | 364 | -0.3136 | -0.1523 |
| seed_p_vs_seed_pars | 272 | -0.4201 | -0.2616 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
