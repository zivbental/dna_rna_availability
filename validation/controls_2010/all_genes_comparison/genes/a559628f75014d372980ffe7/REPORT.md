# YDR210W
Status: ok. Length: 446 nt. Measured usable bases: 338. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 338 | 0.3064 | 0.3116 |
| rnafold | ok | 338 | 0.2785 | 0.2767 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 268 | -0.4398 | -0.3648 |
| seed_p | 268 | -0.1318 | -0.1555 |
| seed_p_vs_seed_pars | 236 | 0.1519 | -0.0554 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
