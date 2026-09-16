# YBR070C
Status: ok. Length: 797 nt. Measured usable bases: 441. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 441 | 0.2633 | 0.2578 |
| rnafold | ok | 441 | 0.2178 | 0.2133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.0979 | -0.3386 |
| seed_p | 96 | -0.2066 | -0.3295 |
| seed_p_vs_seed_pars | 65 | -0.2296 | -0.3412 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
