# YBR241C
Status: ok. Length: 1599 nt. Measured usable bases: 690. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 690 | 0.3743 | 0.3399 |
| rnafold | ok | 690 | 0.2974 | 0.2818 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.1136 | -0.5084 |
| seed_p | 81 | -0.4630 | -0.4528 |
| seed_p_vs_seed_pars | 66 | -0.5677 | -0.5777 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
