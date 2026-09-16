# YGR218W
Status: ok. Length: 3743 nt. Measured usable bases: 2017. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2017 | 0.3235 | 0.3036 |
| rnafold | ok | 2017 | 0.2419 | 0.2250 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 490 | -0.3029 | -0.1889 |
| seed_p | 490 | -0.2654 | -0.1793 |
| seed_p_vs_seed_pars | 379 | -0.4127 | -0.2563 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
