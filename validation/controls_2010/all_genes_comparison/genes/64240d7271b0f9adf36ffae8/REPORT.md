# YGR202C
Status: ok. Length: 1518 nt. Measured usable bases: 643. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 643 | 0.3127 | 0.3237 |
| rnafold | ok | 643 | 0.2831 | 0.2875 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | 0.4923 | 0.2017 |
| seed_p | 97 | -0.1022 | 0.1756 |
| seed_p_vs_seed_pars | 77 | -0.1451 | 0.2246 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
