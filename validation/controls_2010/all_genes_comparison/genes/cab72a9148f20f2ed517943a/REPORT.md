# YGL253W
Status: ok. Length: 1683 nt. Measured usable bases: 1493. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1493 | 0.3079 | 0.2957 |
| rnafold | ok | 1493 | 0.2307 | 0.2269 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1471 | -0.1659 | -0.2330 |
| seed_p | 1471 | -0.4436 | -0.3553 |
| seed_p_vs_seed_pars | 1360 | -0.4524 | -0.3422 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
