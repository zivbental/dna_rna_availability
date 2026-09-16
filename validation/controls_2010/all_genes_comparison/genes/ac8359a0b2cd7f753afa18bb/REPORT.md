# YDR265W
Status: ok. Length: 1297 nt. Measured usable bases: 469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 469 | 0.3613 | 0.3541 |
| rnafold | ok | 469 | 0.2158 | 0.2083 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.4538 | -0.3421 |
| seed_p | 77 | -0.7895 | -0.7137 |
| seed_p_vs_seed_pars | 59 | -0.7275 | -0.7625 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
