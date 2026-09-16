# YGR036C
Status: ok. Length: 720 nt. Measured usable bases: 356. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 356 | 0.2658 | 0.2442 |
| rnafold | ok | 356 | 0.2707 | 0.2866 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.2807 | -0.4678 |
| seed_p | 70 | -0.4672 | -0.5152 |
| seed_p_vs_seed_pars | 40 | -0.2843 | -0.5396 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
