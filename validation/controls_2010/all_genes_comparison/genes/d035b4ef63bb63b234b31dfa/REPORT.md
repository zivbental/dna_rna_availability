# YGR232W
Status: ok. Length: 768 nt. Measured usable bases: 416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 416 | 0.3189 | 0.2804 |
| rnafold | ok | 416 | 0.3166 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | 0.0150 | 0.1126 |
| seed_p | 126 | -0.1128 | -0.1354 |
| seed_p_vs_seed_pars | 80 | -0.4463 | -0.6658 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
