# YDR492W
Status: ok. Length: 1185 nt. Measured usable bases: 580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 580 | 0.2351 | 0.2449 |
| rnafold | ok | 580 | 0.1737 | 0.1832 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 89 | 0.0844 | -0.0135 |
| seed_p | 89 | 0.0385 | 0.0499 |
| seed_p_vs_seed_pars | 60 | -0.5804 | -0.5541 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
