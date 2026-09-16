# YGL238W
Status: ok. Length: 2983 nt. Measured usable bases: 1585. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1585 | 0.2214 | 0.2161 |
| rnafold | ok | 1585 | 0.1827 | 0.1927 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 384 | -0.1155 | 0.0500 |
| seed_p | 384 | 0.1248 | 0.1502 |
| seed_p_vs_seed_pars | 279 | 0.0836 | 0.1031 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
