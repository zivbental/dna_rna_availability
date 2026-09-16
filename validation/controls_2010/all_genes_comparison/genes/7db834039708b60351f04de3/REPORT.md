# YJR048W
Status: ok. Length: 1272 nt. Measured usable bases: 327. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 327 | 0.2252 | 0.2373 |
| rnafold | ok | 327 | 0.1903 | 0.1865 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 167 | -0.0453 | 0.0586 |
| seed_p | 167 | 0.0475 | 0.1899 |
| seed_p_vs_seed_pars | 125 | -0.1479 | -0.1876 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
