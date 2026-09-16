# YPR029C
Status: ok. Length: 2750 nt. Measured usable bases: 1180. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1180 | 0.2764 | 0.2592 |
| rnafold | ok | 1180 | 0.2603 | 0.2444 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.3041 | -0.2365 |
| seed_p | 118 | -0.5074 | -0.3743 |
| seed_p_vs_seed_pars | 71 | -0.4427 | -0.3746 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
