# YDR487C
Status: ok. Length: 764 nt. Measured usable bases: 609. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 609 | 0.3812 | 0.3567 |
| rnafold | ok | 609 | 0.3638 | 0.3374 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 582 | -0.1351 | 0.0758 |
| seed_p | 582 | -0.2242 | -0.0468 |
| seed_p_vs_seed_pars | 513 | -0.2654 | -0.1631 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
