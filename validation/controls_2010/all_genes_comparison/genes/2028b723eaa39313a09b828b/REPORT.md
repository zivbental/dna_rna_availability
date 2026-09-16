# YDR390C
Status: ok. Length: 1985 nt. Measured usable bases: 843. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 843 | 0.2416 | 0.2400 |
| rnafold | ok | 843 | 0.1767 | 0.1787 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | 0.1703 | 0.0246 |
| seed_p | 86 | 0.1933 | -0.0200 |
| seed_p_vs_seed_pars | 75 | 0.1594 | 0.1095 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
