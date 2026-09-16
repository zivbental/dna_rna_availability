# YHR098C
Status: ok. Length: 2987 nt. Measured usable bases: 2000. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2000 | 0.2816 | 0.2697 |
| rnafold | ok | 2000 | 0.2469 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1062 | -0.0329 | 0.1034 |
| seed_p | 1062 | -0.1201 | -0.1025 |
| seed_p_vs_seed_pars | 785 | -0.3171 | -0.2667 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
