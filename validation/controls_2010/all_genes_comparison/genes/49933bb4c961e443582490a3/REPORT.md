# YPL083C
Status: ok. Length: 1511 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.3152 | 0.3180 |
| rnafold | ok | 533 | 0.2274 | 0.2362 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 75 | -0.0920 | -0.1406 |
| seed_p | 75 | 0.2746 | 0.1864 |
| seed_p_vs_seed_pars | 58 | 0.2681 | 0.1414 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
