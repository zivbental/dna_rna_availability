# YMR145C
Status: ok. Length: 1782 nt. Measured usable bases: 1210. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1210 | 0.2963 | 0.2847 |
| rnafold | ok | 1210 | 0.2323 | 0.2340 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 720 | -0.0545 | -0.1186 |
| seed_p | 720 | -0.1178 | -0.0956 |
| seed_p_vs_seed_pars | 539 | -0.3137 | -0.3479 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
