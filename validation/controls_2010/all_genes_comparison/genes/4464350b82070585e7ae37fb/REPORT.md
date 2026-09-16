# YLL019C
Status: ok. Length: 2793 nt. Measured usable bases: 1002. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1002 | 0.3008 | 0.2985 |
| rnafold | ok | 1002 | 0.2197 | 0.2122 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 52 | -0.2717 | -0.5574 |
| seed_p | 52 | -0.4614 | -0.5432 |
| seed_p_vs_seed_pars | 44 | -0.5963 | -0.5728 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
