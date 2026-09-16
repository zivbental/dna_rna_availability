# YOR306C
Status: ok. Length: 1842 nt. Measured usable bases: 796. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 796 | 0.2492 | 0.2323 |
| rnafold | ok | 796 | 0.2559 | 0.2274 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.1425 | 0.0105 |
| seed_p | 138 | -0.4492 | -0.3757 |
| seed_p_vs_seed_pars | 109 | -0.6477 | -0.4611 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
