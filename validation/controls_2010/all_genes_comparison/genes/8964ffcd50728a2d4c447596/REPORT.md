# YNL079C
Status: ok. Length: 788 nt. Measured usable bases: 653. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 653 | 0.4116 | 0.4166 |
| rnafold | ok | 653 | 0.3527 | 0.3644 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 612 | -0.3193 | -0.2643 |
| seed_p | 612 | -0.3004 | -0.2577 |
| seed_p_vs_seed_pars | 539 | -0.3189 | -0.2445 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
