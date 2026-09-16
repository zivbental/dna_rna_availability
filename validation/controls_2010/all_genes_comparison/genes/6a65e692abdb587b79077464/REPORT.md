# YCR053W
Status: ok. Length: 1633 nt. Measured usable bases: 1461. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1461 | 0.2782 | 0.2749 |
| rnafold | ok | 1461 | 0.2272 | 0.2309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1411 | -0.0668 | -0.0812 |
| seed_p | 1411 | -0.1696 | -0.1726 |
| seed_p_vs_seed_pars | 1279 | -0.3501 | -0.2842 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
