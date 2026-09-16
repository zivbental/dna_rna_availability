# YGL106W
Status: ok. Length: 718 nt. Measured usable bases: 498. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 498 | 0.2605 | 0.2653 |
| rnafold | ok | 498 | 0.2429 | 0.2599 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 444 | 0.0350 | 0.0854 |
| seed_p | 444 | 0.1655 | 0.1859 |
| seed_p_vs_seed_pars | 379 | 0.2459 | 0.2496 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
