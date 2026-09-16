# YNR021W
Status: ok. Length: 1422 nt. Measured usable bases: 1113. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1113 | 0.2424 | 0.2406 |
| rnafold | ok | 1113 | 0.1969 | 0.2004 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 931 | 0.0155 | 0.0389 |
| seed_p | 931 | -0.0463 | -0.0496 |
| seed_p_vs_seed_pars | 779 | -0.1126 | -0.1130 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
