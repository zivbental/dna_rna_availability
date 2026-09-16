# YCL055W
Status: ok. Length: 1316 nt. Measured usable bases: 497. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 497 | 0.3009 | 0.2946 |
| rnafold | ok | 497 | 0.2533 | 0.2414 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | -0.5487 | -0.4820 |
| seed_p | 53 | -0.3670 | -0.5176 |
| seed_p_vs_seed_pars | 41 | -0.6214 | -0.7967 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
