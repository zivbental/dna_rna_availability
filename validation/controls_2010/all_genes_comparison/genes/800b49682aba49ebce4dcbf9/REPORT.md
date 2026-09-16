# YEL052W
Status: ok. Length: 1679 nt. Measured usable bases: 1003. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.2975 | 0.2793 |
| rnafold | ok | 1003 | 0.2680 | 0.2631 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 404 | -0.0892 | 0.2030 |
| seed_p | 404 | -0.0205 | 0.0227 |
| seed_p_vs_seed_pars | 357 | -0.1683 | -0.0737 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
