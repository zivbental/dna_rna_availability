# YNL123W
Status: ok. Length: 3166 nt. Measured usable bases: 1497. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1497 | 0.2466 | 0.2118 |
| rnafold | ok | 1497 | 0.2037 | 0.1861 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 265 | -0.0251 | 0.2102 |
| seed_p | 265 | -0.2422 | -0.0282 |
| seed_p_vs_seed_pars | 206 | -0.4981 | -0.0102 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
