# YEL020C
Status: ok. Length: 1683 nt. Measured usable bases: 659. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 659 | 0.3286 | 0.3283 |
| rnafold | ok | 659 | 0.2216 | 0.2306 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.2721 | 0.3764 |
| seed_p | 34 | 0.7173 | 0.6622 |
| seed_p_vs_seed_pars | 23 | 0.6238 | 0.8902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
