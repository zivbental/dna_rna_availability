# YJL192C
Status: ok. Length: 800 nt. Measured usable bases: 575. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 575 | 0.2906 | 0.2872 |
| rnafold | ok | 575 | 0.2461 | 0.2297 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 451 | -0.1085 | 0.0183 |
| seed_p | 451 | -0.2745 | -0.1811 |
| seed_p_vs_seed_pars | 381 | -0.3035 | -0.2417 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
