# YJL016W
Status: ok. Length: 2184 nt. Measured usable bases: 840. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 840 | 0.2885 | 0.2634 |
| rnafold | ok | 840 | 0.1704 | 0.1663 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.3482 | -0.6071 |
| seed_p | 84 | -0.2314 | -0.4359 |
| seed_p_vs_seed_pars | 66 | -0.4888 | -0.6508 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
