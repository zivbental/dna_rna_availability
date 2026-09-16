# YBR067C
Status: ok. Length: 773 nt. Measured usable bases: 627. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 627 | 0.2172 | 0.1992 |
| rnafold | ok | 627 | 0.1267 | 0.1066 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 573 | -0.1740 | 0.1648 |
| seed_p | 573 | -0.0710 | 0.0195 |
| seed_p_vs_seed_pars | 474 | -0.4571 | -0.3797 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
