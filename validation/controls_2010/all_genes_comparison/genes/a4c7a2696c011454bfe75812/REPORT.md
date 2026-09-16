# YBR109C
Status: ok. Length: 644 nt. Measured usable bases: 513. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 513 | 0.2680 | 0.2465 |
| rnafold | ok | 513 | 0.2441 | 0.2100 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 444 | -0.1161 | 0.1304 |
| seed_p | 444 | 0.0500 | 0.1021 |
| seed_p_vs_seed_pars | 338 | 0.0329 | -0.0048 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
