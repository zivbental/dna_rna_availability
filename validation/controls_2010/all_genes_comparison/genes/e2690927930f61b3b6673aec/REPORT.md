# YJR132W
Status: ok. Length: 3388 nt. Measured usable bases: 1598. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1598 | 0.2884 | 0.2836 |
| rnafold | ok | 1598 | 0.2634 | 0.2493 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 281 | -0.2376 | -0.2903 |
| seed_p | 281 | -0.1576 | -0.2645 |
| seed_p_vs_seed_pars | 211 | -0.2099 | -0.3790 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
