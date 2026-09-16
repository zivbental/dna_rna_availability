# YGL155W
Status: ok. Length: 1455 nt. Measured usable bases: 786. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 786 | 0.2506 | 0.2483 |
| rnafold | ok | 786 | 0.2023 | 0.1972 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 189 | 0.0121 | 0.0846 |
| seed_p | 189 | -0.1592 | -0.0854 |
| seed_p_vs_seed_pars | 140 | -0.1217 | -0.0680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
