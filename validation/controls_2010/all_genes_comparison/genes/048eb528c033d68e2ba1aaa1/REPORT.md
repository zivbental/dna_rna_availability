# YLR040C
Status: ok. Length: 798 nt. Measured usable bases: 649. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 649 | 0.1669 | 0.1613 |
| rnafold | ok | 649 | 0.0871 | 0.1032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 564 | -0.1007 | -0.0518 |
| seed_p | 564 | -0.1239 | -0.1329 |
| seed_p_vs_seed_pars | 513 | -0.1998 | -0.2765 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
