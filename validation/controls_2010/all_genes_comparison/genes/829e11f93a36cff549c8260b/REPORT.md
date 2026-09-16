# YLR077W
Status: ok. Length: 1925 nt. Measured usable bases: 840. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 840 | 0.3376 | 0.3291 |
| rnafold | ok | 840 | 0.2779 | 0.2782 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | -0.1246 | -0.3384 |
| seed_p | 124 | -0.2702 | -0.3099 |
| seed_p_vs_seed_pars | 87 | -0.2533 | -0.2918 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
