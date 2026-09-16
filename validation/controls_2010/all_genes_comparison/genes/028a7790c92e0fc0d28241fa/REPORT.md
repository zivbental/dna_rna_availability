# YML077W
Status: ok. Length: 608 nt. Measured usable bases: 309. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 309 | 0.2273 | 0.2366 |
| rnafold | ok | 309 | 0.2558 | 0.2681 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | 0.2752 | 0.2071 |
| seed_p | 97 | 0.0163 | 0.1644 |
| seed_p_vs_seed_pars | 96 | -0.1446 | -0.1473 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
