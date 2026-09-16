# YOL010W
Status: ok. Length: 1272 nt. Measured usable bases: 610. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 610 | 0.3237 | 0.2889 |
| rnafold | ok | 610 | 0.3168 | 0.2785 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.1680 | 0.0688 |
| seed_p | 71 | 0.2371 | 0.2927 |
| seed_p_vs_seed_pars | 40 | 0.4799 | 0.3636 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
