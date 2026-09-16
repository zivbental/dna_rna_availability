# YBR229C
Status: ok. Length: 2991 nt. Measured usable bases: 1564. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1564 | 0.2516 | 0.2417 |
| rnafold | ok | 1564 | 0.2407 | 0.2364 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 290 | -0.0779 | -0.0678 |
| seed_p | 290 | -0.1253 | -0.1679 |
| seed_p_vs_seed_pars | 223 | -0.2620 | -0.2506 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
