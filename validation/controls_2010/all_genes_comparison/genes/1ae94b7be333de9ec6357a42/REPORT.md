# YDR035W
Status: ok. Length: 1424 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.3211 | 0.3094 |
| rnafold | ok | 846 | 0.3066 | 0.2899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 412 | 0.1550 | 0.0483 |
| seed_p | 412 | 0.0405 | 0.0089 |
| seed_p_vs_seed_pars | 323 | 0.2033 | -0.0148 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
