# YBR127C
Status: ok. Length: 1748 nt. Measured usable bases: 1432. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1432 | 0.3465 | 0.3289 |
| rnafold | ok | 1432 | 0.2912 | 0.2872 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1272 | -0.1044 | -0.0073 |
| seed_p | 1272 | -0.1104 | -0.0592 |
| seed_p_vs_seed_pars | 1133 | -0.2488 | -0.2093 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
