# YBR291C
Status: ok. Length: 1091 nt. Measured usable bases: 479. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 479 | 0.3567 | 0.3554 |
| rnafold | ok | 479 | 0.3443 | 0.3482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.1533 | -0.0111 |
| seed_p | 72 | -0.0309 | -0.0690 |
| seed_p_vs_seed_pars | 43 | -0.2605 | 0.0228 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
