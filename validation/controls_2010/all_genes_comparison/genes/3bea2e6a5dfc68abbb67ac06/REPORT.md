# YML014W
Status: ok. Length: 956 nt. Measured usable bases: 455. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 455 | 0.3106 | 0.3082 |
| rnafold | ok | 455 | 0.2677 | 0.2712 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | -0.5365 | -0.4589 |
| seed_p | 90 | -0.5462 | -0.5447 |
| seed_p_vs_seed_pars | 70 | -0.5389 | -0.5273 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
