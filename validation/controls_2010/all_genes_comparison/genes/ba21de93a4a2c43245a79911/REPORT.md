# YLR188W
Status: ok. Length: 2297 nt. Measured usable bases: 1162. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1162 | 0.3265 | 0.3013 |
| rnafold | ok | 1162 | 0.2449 | 0.2104 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | 0.1636 | 0.1647 |
| seed_p | 211 | -0.1068 | -0.0647 |
| seed_p_vs_seed_pars | 157 | -0.3798 | -0.3082 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
