# YNL159C
Status: ok. Length: 1202 nt. Measured usable bases: 562. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 562 | 0.3259 | 0.3175 |
| rnafold | ok | 562 | 0.2013 | 0.1982 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | 0.2100 | 0.1688 |
| seed_p | 96 | 0.4408 | 0.3338 |
| seed_p_vs_seed_pars | 64 | 0.5892 | 0.5562 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
