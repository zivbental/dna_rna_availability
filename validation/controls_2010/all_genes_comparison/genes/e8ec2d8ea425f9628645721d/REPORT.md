# YNL329C
Status: ok. Length: 3217 nt. Measured usable bases: 1171. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1171 | 0.2868 | 0.2745 |
| rnafold | ok | 1171 | 0.2081 | 0.2041 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.6639 | -0.6576 |
| seed_p | 36 | -0.3255 | -0.4903 |
| seed_p_vs_seed_pars | 25 | -0.7487 | -0.7214 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
