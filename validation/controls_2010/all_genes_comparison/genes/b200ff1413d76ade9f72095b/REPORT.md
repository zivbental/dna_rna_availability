# YGR080W
Status: ok. Length: 1077 nt. Measured usable bases: 575. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 575 | 0.2667 | 0.2825 |
| rnafold | ok | 575 | 0.2308 | 0.2342 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | -0.1409 | -0.1260 |
| seed_p | 162 | 0.1455 | 0.1771 |
| seed_p_vs_seed_pars | 142 | 0.1078 | 0.1632 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
