# YDR489W
Status: ok. Length: 885 nt. Measured usable bases: 396. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 396 | 0.2384 | 0.2336 |
| rnafold | ok | 396 | 0.1776 | 0.1620 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | 0.3770 | 0.3608 |
| seed_p | 51 | 0.3493 | 0.7406 |
| seed_p_vs_seed_pars | 39 | 0.2330 | 0.6086 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
