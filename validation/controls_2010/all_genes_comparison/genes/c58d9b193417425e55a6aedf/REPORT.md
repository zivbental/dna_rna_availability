# YGR033C
Status: ok. Length: 1052 nt. Measured usable bases: 604. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 604 | 0.2774 | 0.2544 |
| rnafold | ok | 604 | 0.1905 | 0.1852 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 204 | -0.1095 | -0.3946 |
| seed_p | 204 | -0.3320 | -0.2730 |
| seed_p_vs_seed_pars | 145 | -0.4420 | -0.3523 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
