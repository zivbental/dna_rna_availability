# YBR276C
Status: ok. Length: 2551 nt. Measured usable bases: 1265. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1265 | 0.3209 | 0.3173 |
| rnafold | ok | 1265 | 0.3106 | 0.3138 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 207 | 0.0265 | 0.2455 |
| seed_p | 207 | 0.0739 | 0.1451 |
| seed_p_vs_seed_pars | 150 | -0.3390 | -0.2259 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
