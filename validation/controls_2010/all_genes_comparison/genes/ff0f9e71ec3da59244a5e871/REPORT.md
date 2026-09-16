# YBR273C
Status: ok. Length: 1438 nt. Measured usable bases: 648. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 648 | 0.3592 | 0.3580 |
| rnafold | ok | 648 | 0.2906 | 0.3025 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.3723 | -0.3315 |
| seed_p | 72 | -0.7151 | -0.5427 |
| seed_p_vs_seed_pars | 47 | -0.6589 | -0.7022 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
