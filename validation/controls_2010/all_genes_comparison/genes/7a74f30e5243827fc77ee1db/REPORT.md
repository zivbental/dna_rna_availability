# YDR168W
Status: ok. Length: 1649 nt. Measured usable bases: 731. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 731 | 0.3714 | 0.3632 |
| rnafold | ok | 731 | 0.3174 | 0.3299 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 122 | -0.1583 | -0.3528 |
| seed_p | 122 | -0.5042 | -0.3074 |
| seed_p_vs_seed_pars | 88 | -0.6339 | -0.2495 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
