# YOL064C
Status: ok. Length: 1164 nt. Measured usable bases: 735. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 735 | 0.3691 | 0.3594 |
| rnafold | ok | 735 | 0.3141 | 0.3182 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 361 | -0.1775 | -0.3412 |
| seed_p | 361 | -0.2984 | -0.3469 |
| seed_p_vs_seed_pars | 280 | -0.3240 | -0.5100 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
