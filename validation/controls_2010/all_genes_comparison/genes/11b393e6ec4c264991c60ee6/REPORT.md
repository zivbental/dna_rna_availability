# YDL040C
Status: ok. Length: 2680 nt. Measured usable bases: 1569. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1569 | 0.3327 | 0.3258 |
| rnafold | ok | 1569 | 0.3103 | 0.3104 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 473 | -0.1215 | -0.3175 |
| seed_p | 473 | -0.1801 | -0.1363 |
| seed_p_vs_seed_pars | 396 | -0.1992 | -0.1098 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
