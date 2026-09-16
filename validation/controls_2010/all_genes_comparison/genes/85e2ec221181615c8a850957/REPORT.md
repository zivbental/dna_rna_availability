# YBR246W
Status: ok. Length: 1295 nt. Measured usable bases: 832. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 832 | 0.2388 | 0.2210 |
| rnafold | ok | 832 | 0.1759 | 0.1546 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 335 | -0.0321 | 0.0552 |
| seed_p | 335 | 0.1477 | 0.0187 |
| seed_p_vs_seed_pars | 257 | 0.0022 | -0.1923 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
