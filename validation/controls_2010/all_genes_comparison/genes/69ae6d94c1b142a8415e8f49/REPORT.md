# YPR023C
Status: ok. Length: 1298 nt. Measured usable bases: 684. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 684 | 0.3604 | 0.3482 |
| rnafold | ok | 684 | 0.3363 | 0.3247 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | 0.3835 | 0.0073 |
| seed_p | 82 | 0.0827 | -0.0144 |
| seed_p_vs_seed_pars | 44 | -0.0569 | -0.1902 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
