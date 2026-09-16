# YJL138C
Status: ok. Length: 1442 nt. Measured usable bases: 260. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 260 | 0.2972 | 0.3039 |
| rnafold | ok | 260 | 0.2331 | 0.2343 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 146 | -0.3835 | -0.5549 |
| seed_p | 146 | -0.2714 | -0.3894 |
| seed_p_vs_seed_pars | 135 | -0.2263 | -0.4313 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
