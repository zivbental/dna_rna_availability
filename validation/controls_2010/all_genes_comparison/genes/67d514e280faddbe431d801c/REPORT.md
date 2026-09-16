# YGR239C
Status: ok. Length: 1092 nt. Measured usable bases: 331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 331 | 0.3068 | 0.2911 |
| rnafold | ok | 331 | 0.2493 | 0.2383 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.0092 | -0.2909 |
| seed_p | 45 | -0.7529 | -0.8099 |
| seed_p_vs_seed_pars | 45 | -0.5593 | -0.4779 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
