# YDL182W
Status: ok. Length: 1401 nt. Measured usable bases: 582. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 582 | 0.3293 | 0.3227 |
| rnafold | ok | 582 | 0.2534 | 0.2594 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 352 | -0.0186 | 0.0863 |
| seed_p | 352 | -0.0508 | 0.0395 |
| seed_p_vs_seed_pars | 261 | -0.0046 | 0.0250 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
