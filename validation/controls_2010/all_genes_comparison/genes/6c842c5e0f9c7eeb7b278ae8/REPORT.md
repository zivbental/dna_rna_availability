# YHR121W
Status: ok. Length: 731 nt. Measured usable bases: 438. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 438 | 0.2673 | 0.2633 |
| rnafold | ok | 438 | 0.2714 | 0.2840 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | 0.3288 | 0.3262 |
| seed_p | 176 | 0.2924 | 0.2608 |
| seed_p_vs_seed_pars | 155 | 0.3575 | 0.3520 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
