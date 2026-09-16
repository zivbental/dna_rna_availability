# YLR409C
Status: ok. Length: 2878 nt. Measured usable bases: 1546. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1546 | 0.3109 | 0.2977 |
| rnafold | ok | 1546 | 0.2364 | 0.2389 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 248 | 0.3135 | 0.1590 |
| seed_p | 248 | -0.2746 | -0.2991 |
| seed_p_vs_seed_pars | 204 | -0.4742 | -0.4587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
