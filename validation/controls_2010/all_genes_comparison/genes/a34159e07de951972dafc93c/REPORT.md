# YKL021C
Status: ok. Length: 1473 nt. Measured usable bases: 605. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 605 | 0.3574 | 0.3580 |
| rnafold | ok | 605 | 0.2730 | 0.2803 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.1591 | 0.1786 |
| seed_p | 54 | -0.4856 | -0.3761 |
| seed_p_vs_seed_pars | 45 | -0.2026 | -0.1324 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
