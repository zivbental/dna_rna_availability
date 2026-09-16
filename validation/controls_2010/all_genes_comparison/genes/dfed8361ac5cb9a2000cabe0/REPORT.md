# YGR008C
Status: ok. Length: 464 nt. Measured usable bases: 204. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 204 | 0.3767 | 0.3746 |
| rnafold | ok | 204 | 0.2505 | 0.2744 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 74 | 0.1801 | -0.1821 |
| seed_p | 74 | 0.0821 | -0.0160 |
| seed_p_vs_seed_pars | 45 | -0.1441 | -0.4030 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
