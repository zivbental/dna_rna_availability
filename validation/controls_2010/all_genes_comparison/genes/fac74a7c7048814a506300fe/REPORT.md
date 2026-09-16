# YNR044W
Status: ok. Length: 2275 nt. Measured usable bases: 1106. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1106 | 0.1386 | 0.1312 |
| rnafold | ok | 1106 | 0.1174 | 0.1000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 245 | -0.0733 | -0.2273 |
| seed_p | 245 | -0.0797 | -0.1145 |
| seed_p_vs_seed_pars | 194 | -0.0972 | -0.0552 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
