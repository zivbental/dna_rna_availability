# YOL013C
Status: ok. Length: 1933 nt. Measured usable bases: 740. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 740 | 0.3064 | 0.2875 |
| rnafold | ok | 740 | 0.2843 | 0.2687 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.3490 | -0.3320 |
| seed_p | 72 | -0.4333 | -0.4929 |
| seed_p_vs_seed_pars | 50 | -0.3469 | -0.2287 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
