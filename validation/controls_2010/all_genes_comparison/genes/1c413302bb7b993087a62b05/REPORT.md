# YLR443W
Status: ok. Length: 1347 nt. Measured usable bases: 684. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 684 | 0.2900 | 0.2705 |
| rnafold | ok | 684 | 0.2936 | 0.2707 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.2554 | -0.0479 |
| seed_p | 135 | -0.0219 | -0.0404 |
| seed_p_vs_seed_pars | 85 | -0.1430 | 0.0469 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
