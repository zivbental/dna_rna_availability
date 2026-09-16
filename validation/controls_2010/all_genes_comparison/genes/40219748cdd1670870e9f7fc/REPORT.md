# YML038C
Status: ok. Length: 1622 nt. Measured usable bases: 725. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 725 | 0.2519 | 0.2354 |
| rnafold | ok | 725 | 0.2311 | 0.2236 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 125 | 0.0490 | 0.1708 |
| seed_p | 125 | -0.2105 | -0.0494 |
| seed_p_vs_seed_pars | 88 | -0.4656 | -0.2209 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
