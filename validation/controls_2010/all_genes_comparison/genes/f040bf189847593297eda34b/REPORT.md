# YFR032C-A
Status: ok. Length: 588 nt. Measured usable bases: 226. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 226 | 0.1420 | 0.1148 |
| rnafold | ok | 226 | 0.2113 | 0.2133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | 0.1899 | 0.1027 |
| seed_p | 205 | 0.1904 | 0.1050 |
| seed_p_vs_seed_pars | 193 | 0.3132 | 0.2283 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
