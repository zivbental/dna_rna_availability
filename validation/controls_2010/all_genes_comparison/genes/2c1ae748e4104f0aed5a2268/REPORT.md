# YBR104W
Status: ok. Length: 1137 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.3580 | 0.3426 |
| rnafold | ok | 633 | 0.3467 | 0.3330 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | 0.4309 | 0.2410 |
| seed_p | 128 | -0.2583 | -0.0721 |
| seed_p_vs_seed_pars | 102 | -0.5821 | -0.5644 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
