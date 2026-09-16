# YMR129W
Status: ok. Length: 4180 nt. Measured usable bases: 1979. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1979 | 0.2888 | 0.2659 |
| rnafold | ok | 1979 | 0.2492 | 0.2389 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 361 | -0.3230 | -0.0926 |
| seed_p | 361 | -0.3677 | -0.2149 |
| seed_p_vs_seed_pars | 239 | -0.3455 | -0.2501 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
