# YOR224C
Status: ok. Length: 533 nt. Measured usable bases: 488. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.2121 | 0.1849 |
| rnafold | ok | 488 | 0.1502 | 0.1240 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 470 | 0.0061 | 0.0350 |
| seed_p | 470 | -0.1916 | -0.1469 |
| seed_p_vs_seed_pars | 443 | -0.2677 | -0.1634 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
