# YOR204W
Status: ok. Length: 2558 nt. Measured usable bases: 1911. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1911 | 0.3464 | 0.3534 |
| rnafold | ok | 1911 | 0.2711 | 0.2769 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1545 | -0.0838 | -0.2201 |
| seed_p | 1545 | -0.2120 | -0.1910 |
| seed_p_vs_seed_pars | 1265 | -0.4238 | -0.3838 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
