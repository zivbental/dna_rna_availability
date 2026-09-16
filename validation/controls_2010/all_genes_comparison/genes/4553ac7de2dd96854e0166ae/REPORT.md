# YOL077W-A
Status: ok. Length: 345 nt. Measured usable bases: 188. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 188 | 0.2942 | 0.2854 |
| rnafold | ok | 188 | 0.3034 | 0.2921 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.3276 | -0.0213 |
| seed_p | 82 | -0.3042 | -0.2444 |
| seed_p_vs_seed_pars | 66 | -0.0481 | 0.0245 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
