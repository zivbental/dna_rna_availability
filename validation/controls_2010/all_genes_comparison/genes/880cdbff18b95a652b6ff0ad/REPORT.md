# YKR044W
Status: ok. Length: 1459 nt. Measured usable bases: 649. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 649 | 0.3504 | 0.3656 |
| rnafold | ok | 649 | 0.2782 | 0.2991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | 0.0640 | 0.0512 |
| seed_p | 63 | 0.5619 | 0.5517 |
| seed_p_vs_seed_pars | 39 | 0.3292 | 0.0567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
