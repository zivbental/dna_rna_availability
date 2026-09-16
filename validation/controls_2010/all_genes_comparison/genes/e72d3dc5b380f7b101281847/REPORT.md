# YEL017C-A
Status: ok. Length: 609 nt. Measured usable bases: 476. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 476 | 0.3139 | 0.2894 |
| rnafold | ok | 476 | 0.3177 | 0.3094 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 381 | -0.1752 | -0.2633 |
| seed_p | 381 | -0.1388 | -0.1724 |
| seed_p_vs_seed_pars | 316 | -0.0581 | -0.0966 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
