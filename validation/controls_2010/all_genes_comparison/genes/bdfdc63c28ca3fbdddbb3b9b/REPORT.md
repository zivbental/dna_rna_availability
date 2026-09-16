# YCR060W
Status: ok. Length: 475 nt. Measured usable bases: 258. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 258 | 0.3107 | 0.3306 |
| rnafold | ok | 258 | 0.2865 | 0.3257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | 0.1360 | -0.1147 |
| seed_p | 134 | -0.0360 | -0.1354 |
| seed_p_vs_seed_pars | 129 | 0.0899 | -0.0651 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
