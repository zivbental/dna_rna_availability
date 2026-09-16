# YLR388W
Status: ok. Length: 740 nt. Measured usable bases: 343. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 343 | 0.2945 | 0.2969 |
| rnafold | ok | 343 | 0.2843 | 0.2842 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.3491 | -0.7267 |
| seed_p | 127 | -0.4909 | -0.4989 |
| seed_p_vs_seed_pars | 110 | -0.5490 | -0.5955 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
