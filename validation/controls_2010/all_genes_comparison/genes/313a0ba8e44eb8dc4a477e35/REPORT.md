# YER019W
Status: ok. Length: 1634 nt. Measured usable bases: 963. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 963 | 0.2733 | 0.2372 |
| rnafold | ok | 963 | 0.2599 | 0.2207 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 504 | -0.3051 | -0.1069 |
| seed_p | 504 | -0.1412 | -0.1647 |
| seed_p_vs_seed_pars | 408 | -0.2039 | -0.2861 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
