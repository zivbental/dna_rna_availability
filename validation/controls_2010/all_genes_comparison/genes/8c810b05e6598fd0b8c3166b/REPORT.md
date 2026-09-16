# YDR056C
Status: ok. Length: 764 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.2870 | 0.2886 |
| rnafold | ok | 506 | 0.2893 | 0.2883 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 328 | -0.0018 | -0.1743 |
| seed_p | 328 | 0.0618 | -0.0653 |
| seed_p_vs_seed_pars | 257 | -0.1122 | -0.1719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
