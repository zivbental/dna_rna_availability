# YOR145C
Status: ok. Length: 895 nt. Measured usable bases: 605. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 605 | 0.2772 | 0.2676 |
| rnafold | ok | 605 | 0.2589 | 0.2664 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 369 | -0.2007 | -0.0665 |
| seed_p | 369 | -0.1218 | -0.1469 |
| seed_p_vs_seed_pars | 270 | -0.2011 | -0.2046 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
