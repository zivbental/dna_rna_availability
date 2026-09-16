# YJR124C
Status: ok. Length: 1628 nt. Measured usable bases: 961. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 961 | 0.2696 | 0.2455 |
| rnafold | ok | 961 | 0.2691 | 0.2480 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 351 | -0.0477 | 0.2082 |
| seed_p | 351 | -0.0435 | -0.0011 |
| seed_p_vs_seed_pars | 263 | -0.1739 | -0.0833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
