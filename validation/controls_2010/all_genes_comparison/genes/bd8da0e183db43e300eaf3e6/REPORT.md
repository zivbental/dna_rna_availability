# YIL046W
Status: ok. Length: 2116 nt. Measured usable bases: 965. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 965 | 0.3005 | 0.2862 |
| rnafold | ok | 965 | 0.2767 | 0.2730 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 161 | -0.0116 | 0.1516 |
| seed_p | 161 | 0.1234 | 0.1889 |
| seed_p_vs_seed_pars | 114 | 0.4499 | 0.5208 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
