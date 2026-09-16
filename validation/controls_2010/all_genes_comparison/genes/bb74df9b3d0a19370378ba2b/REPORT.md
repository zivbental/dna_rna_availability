# YGR063C
Status: ok. Length: 389 nt. Measured usable bases: 234. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 234 | 0.3774 | 0.3910 |
| rnafold | ok | 234 | 0.3601 | 0.3748 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | 0.0682 | -0.1715 |
| seed_p | 155 | 0.0421 | -0.0988 |
| seed_p_vs_seed_pars | 102 | -0.0053 | 0.0264 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
