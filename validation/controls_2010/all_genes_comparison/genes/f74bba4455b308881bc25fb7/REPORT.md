# YGR102C
Status: ok. Length: 707 nt. Measured usable bases: 253. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 253 | 0.3650 | 0.3836 |
| rnafold | ok | 253 | 0.2283 | 0.2527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | 0.4715 | 0.3688 |
| seed_p | 48 | 0.7182 | 0.6951 |
| seed_p_vs_seed_pars | 39 | 0.5199 | 0.5661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
