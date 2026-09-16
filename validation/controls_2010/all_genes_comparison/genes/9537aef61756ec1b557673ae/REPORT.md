# YGR191W
Status: ok. Length: 2183 nt. Measured usable bases: 1597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1597 | 0.2460 | 0.2318 |
| rnafold | ok | 1597 | 0.1473 | 0.1503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1013 | -0.1304 | -0.2786 |
| seed_p | 1013 | -0.2684 | -0.1796 |
| seed_p_vs_seed_pars | 766 | -0.3148 | -0.2150 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
