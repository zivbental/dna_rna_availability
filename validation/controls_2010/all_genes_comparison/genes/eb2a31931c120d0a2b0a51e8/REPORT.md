# YDR341C
Status: ok. Length: 2021 nt. Measured usable bases: 1524. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1524 | 0.3811 | 0.3663 |
| rnafold | ok | 1524 | 0.3034 | 0.2838 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1087 | -0.2246 | -0.2219 |
| seed_p | 1087 | -0.1990 | -0.2330 |
| seed_p_vs_seed_pars | 934 | -0.4160 | -0.3990 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
