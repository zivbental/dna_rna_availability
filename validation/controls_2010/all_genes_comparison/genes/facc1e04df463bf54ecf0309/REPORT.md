# YPL163C
Status: ok. Length: 1089 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.2148 | 0.2069 |
| rnafold | ok | 846 | 0.1978 | 0.1940 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 727 | -0.1294 | -0.0319 |
| seed_p | 727 | -0.1958 | -0.2289 |
| seed_p_vs_seed_pars | 616 | -0.2254 | -0.2391 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
