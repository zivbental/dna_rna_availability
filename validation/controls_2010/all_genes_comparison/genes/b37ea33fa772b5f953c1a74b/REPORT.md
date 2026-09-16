# YNL292W
Status: ok. Length: 1213 nt. Measured usable bases: 445. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 445 | -0.0103 | -0.0040 |
| rnafold | ok | 445 | 0.0178 | 0.0103 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.5044 | -0.3312 |
| seed_p | 34 | 0.2061 | 0.2119 |
| seed_p_vs_seed_pars | 24 | 0.6961 | 0.4909 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
