# YBR125C
Status: ok. Length: 1528 nt. Measured usable bases: 675. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 675 | 0.2805 | 0.2770 |
| rnafold | ok | 675 | 0.2109 | 0.2132 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | -0.0719 | 0.0983 |
| seed_p | 155 | -0.2288 | -0.2695 |
| seed_p_vs_seed_pars | 129 | -0.4340 | -0.3348 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
