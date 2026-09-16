# YJR060W
Status: ok. Length: 1769 nt. Measured usable bases: 872. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 872 | 0.3434 | 0.3381 |
| rnafold | ok | 872 | 0.2344 | 0.2336 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 194 | -0.0999 | 0.1093 |
| seed_p | 194 | 0.1912 | 0.2174 |
| seed_p_vs_seed_pars | 173 | 0.0866 | 0.1146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
