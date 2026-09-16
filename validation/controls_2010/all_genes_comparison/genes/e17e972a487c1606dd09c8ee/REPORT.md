# YNR061C
Status: ok. Length: 1033 nt. Measured usable bases: 747. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 747 | 0.1984 | 0.1697 |
| rnafold | ok | 747 | 0.2213 | 0.1897 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 445 | 0.0748 | 0.1396 |
| seed_p | 445 | -0.0925 | -0.0184 |
| seed_p_vs_seed_pars | 346 | -0.1937 | -0.1781 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
