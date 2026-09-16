# YDR148C
Status: ok. Length: 1724 nt. Measured usable bases: 992. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 992 | 0.3362 | 0.3208 |
| rnafold | ok | 992 | 0.3003 | 0.2803 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 313 | 0.0889 | 0.1457 |
| seed_p | 313 | -0.0529 | -0.0803 |
| seed_p_vs_seed_pars | 223 | -0.1403 | -0.0022 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
