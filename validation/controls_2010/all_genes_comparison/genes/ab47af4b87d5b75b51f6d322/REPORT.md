# YCR073W-A
Status: ok. Length: 1077 nt. Measured usable bases: 580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 580 | 0.2543 | 0.2516 |
| rnafold | ok | 580 | 0.1827 | 0.1975 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 216 | 0.0532 | 0.1661 |
| seed_p | 216 | 0.1395 | 0.1018 |
| seed_p_vs_seed_pars | 180 | 0.0196 | 0.0516 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
