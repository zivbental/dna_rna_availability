# YHR025W
Status: ok. Length: 1182 nt. Measured usable bases: 1005. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1005 | 0.3123 | 0.2823 |
| rnafold | ok | 1005 | 0.3004 | 0.2734 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 924 | -0.0237 | -0.0109 |
| seed_p | 924 | -0.1242 | -0.0721 |
| seed_p_vs_seed_pars | 857 | -0.1812 | -0.1885 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
