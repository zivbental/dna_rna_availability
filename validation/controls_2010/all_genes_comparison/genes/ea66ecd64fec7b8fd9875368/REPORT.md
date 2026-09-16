# YEL058W
Status: ok. Length: 1782 nt. Measured usable bases: 1401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1401 | 0.3386 | 0.3042 |
| rnafold | ok | 1401 | 0.2619 | 0.2566 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1164 | -0.0500 | -0.0958 |
| seed_p | 1164 | -0.2396 | -0.1827 |
| seed_p_vs_seed_pars | 992 | -0.3793 | -0.2488 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
