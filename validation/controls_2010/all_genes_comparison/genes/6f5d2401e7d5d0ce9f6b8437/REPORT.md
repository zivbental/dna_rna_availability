# YOL097C
Status: ok. Length: 1438 nt. Measured usable bases: 1195. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1195 | 0.3210 | 0.3090 |
| rnafold | ok | 1195 | 0.2420 | 0.2515 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1048 | -0.0618 | -0.1939 |
| seed_p | 1048 | -0.2508 | -0.2861 |
| seed_p_vs_seed_pars | 903 | -0.3579 | -0.3820 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
