# YGL091C
Status: ok. Length: 1175 nt. Measured usable bases: 515. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 515 | 0.2642 | 0.2750 |
| rnafold | ok | 515 | 0.2637 | 0.3122 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | -0.4112 | -0.5129 |
| seed_p | 91 | 0.2729 | 0.1129 |
| seed_p_vs_seed_pars | 62 | 0.2833 | 0.1221 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
