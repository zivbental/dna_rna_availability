# YLR153C
Status: ok. Length: 2344 nt. Measured usable bases: 1953. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1953 | 0.2646 | 0.2502 |
| rnafold | ok | 1953 | 0.1910 | 0.1839 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1763 | -0.0833 | -0.1188 |
| seed_p | 1763 | -0.1520 | -0.1354 |
| seed_p_vs_seed_pars | 1409 | -0.2096 | -0.2400 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
