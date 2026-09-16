# YGR099W
Status: ok. Length: 2157 nt. Measured usable bases: 795. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 795 | 0.2786 | 0.2638 |
| rnafold | ok | 795 | 0.2519 | 0.2453 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 79 | 0.1424 | 0.0704 |
| seed_p | 79 | -0.2660 | -0.3480 |
| seed_p_vs_seed_pars | 64 | 0.2681 | 0.1917 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
