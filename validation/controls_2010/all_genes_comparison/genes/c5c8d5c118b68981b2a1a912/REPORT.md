# YDR267C
Status: ok. Length: 1179 nt. Measured usable bases: 559. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 559 | 0.3320 | 0.2995 |
| rnafold | ok | 559 | 0.2970 | 0.2748 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.7561 | 0.0873 |
| seed_p | 39 | -0.6868 | -0.5139 |
| seed_p_vs_seed_pars | 37 | -0.4820 | -0.5588 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
