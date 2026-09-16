# YNL003C
Status: ok. Length: 1060 nt. Measured usable bases: 513. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 513 | 0.3145 | 0.3217 |
| rnafold | ok | 513 | 0.2459 | 0.2610 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.0781 | -0.2769 |
| seed_p | 109 | -0.2483 | -0.1794 |
| seed_p_vs_seed_pars | 79 | -0.6132 | -0.4627 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
