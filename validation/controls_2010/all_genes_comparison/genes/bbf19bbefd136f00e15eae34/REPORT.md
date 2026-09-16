# YDR508C
Status: ok. Length: 2333 nt. Measured usable bases: 1711. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1711 | 0.2703 | 0.2768 |
| rnafold | ok | 1711 | 0.2270 | 0.2206 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1239 | -0.1848 | -0.2388 |
| seed_p | 1239 | -0.0862 | -0.1312 |
| seed_p_vs_seed_pars | 1069 | -0.1562 | -0.2140 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
