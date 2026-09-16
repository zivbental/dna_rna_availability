# YOR176W
Status: ok. Length: 1414 nt. Measured usable bases: 920. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 920 | 0.3658 | 0.3479 |
| rnafold | ok | 920 | 0.2709 | 0.2766 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 530 | -0.0005 | -0.0720 |
| seed_p | 530 | -0.0704 | -0.1359 |
| seed_p_vs_seed_pars | 466 | -0.1543 | -0.1440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
