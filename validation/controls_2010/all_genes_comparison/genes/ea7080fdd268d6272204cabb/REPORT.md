# YPL012W
Status: ok. Length: 3913 nt. Measured usable bases: 1749. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1749 | 0.2762 | 0.2643 |
| rnafold | ok | 1749 | 0.2242 | 0.2151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.2457 | -0.0526 |
| seed_p | 203 | 0.0236 | 0.0518 |
| seed_p_vs_seed_pars | 121 | 0.1828 | 0.3146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
