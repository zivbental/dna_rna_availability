# YPL187W
Status: ok. Length: 498 nt. Measured usable bases: 268. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 268 | 0.2831 | 0.2904 |
| rnafold | ok | 268 | 0.3729 | 0.3747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 235 | -0.3335 | -0.1776 |
| seed_p | 235 | -0.0445 | -0.0609 |
| seed_p_vs_seed_pars | 231 | -0.2149 | -0.2571 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
