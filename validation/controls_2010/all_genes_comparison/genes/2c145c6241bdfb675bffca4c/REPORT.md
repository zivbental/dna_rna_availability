# YDR073W
Status: ok. Length: 1157 nt. Measured usable bases: 363. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 363 | 0.3404 | 0.3454 |
| rnafold | ok | 363 | 0.2802 | 0.3037 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | -0.2690 | -0.5270 |
| seed_p | 63 | -0.5793 | -0.5112 |
| seed_p_vs_seed_pars | 52 | -0.5230 | -0.5147 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
