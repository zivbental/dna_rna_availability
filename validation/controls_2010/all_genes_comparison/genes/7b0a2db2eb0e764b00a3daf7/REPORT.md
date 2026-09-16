# YCL005W
Status: ok. Length: 929 nt. Measured usable bases: 588. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 588 | 0.2422 | 0.2305 |
| rnafold | ok | 588 | 0.1828 | 0.1872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 365 | 0.0334 | -0.0078 |
| seed_p | 365 | 0.0718 | 0.0547 |
| seed_p_vs_seed_pars | 273 | 0.2439 | 0.2442 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
