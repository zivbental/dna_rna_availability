# YPL092W
Status: ok. Length: 1590 nt. Measured usable bases: 834. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 834 | 0.3117 | 0.3118 |
| rnafold | ok | 834 | 0.2362 | 0.2306 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | -0.2782 | -0.2981 |
| seed_p | 159 | -0.2134 | -0.3041 |
| seed_p_vs_seed_pars | 122 | -0.2668 | -0.2306 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
