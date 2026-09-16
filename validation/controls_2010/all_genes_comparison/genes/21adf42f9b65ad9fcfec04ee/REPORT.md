# YOR272W
Status: ok. Length: 1501 nt. Measured usable bases: 914. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 914 | 0.2366 | 0.2157 |
| rnafold | ok | 914 | 0.1893 | 0.1887 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 373 | -0.0544 | -0.1291 |
| seed_p | 373 | -0.2200 | -0.2239 |
| seed_p_vs_seed_pars | 277 | -0.1623 | -0.2373 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
