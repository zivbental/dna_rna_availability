# YGL010W
Status: ok. Length: 750 nt. Measured usable bases: 300. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 300 | 0.3488 | 0.3611 |
| rnafold | ok | 300 | 0.3435 | 0.3469 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | 0.4222 | 0.8546 |
| seed_p | 27 | 0.5012 | 0.6749 |
| seed_p_vs_seed_pars | 21 | -0.2047 | 0.1948 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
