# YLR355C
Status: ok. Length: 1445 nt. Measured usable bases: 1326. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1326 | 0.3069 | 0.2832 |
| rnafold | ok | 1326 | 0.2695 | 0.2509 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1264 | -0.1681 | -0.0671 |
| seed_p | 1264 | -0.2141 | -0.1497 |
| seed_p_vs_seed_pars | 1226 | -0.2554 | -0.2343 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
