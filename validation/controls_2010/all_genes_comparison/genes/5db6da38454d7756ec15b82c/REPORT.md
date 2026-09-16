# YDR182W
Status: ok. Length: 1600 nt. Measured usable bases: 817. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 817 | 0.1946 | 0.1904 |
| rnafold | ok | 817 | 0.1718 | 0.1650 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 220 | 0.3846 | 0.3728 |
| seed_p | 220 | 0.3769 | 0.2992 |
| seed_p_vs_seed_pars | 170 | 0.0339 | -0.0371 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
