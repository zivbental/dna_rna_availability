# YDL231C
Status: ok. Length: 3378 nt. Measured usable bases: 1527. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1527 | 0.2173 | 0.2069 |
| rnafold | ok | 1527 | 0.1463 | 0.1441 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 236 | 0.0345 | -0.0834 |
| seed_p | 236 | 0.1333 | 0.0669 |
| seed_p_vs_seed_pars | 161 | -0.1307 | -0.0756 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
