# YDL184C
Status: ok. Length: 290 nt. Measured usable bases: 197. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 197 | 0.3925 | 0.3612 |
| rnafold | ok | 197 | 0.3851 | 0.3540 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | 0.0041 | 0.0650 |
| seed_p | 174 | 0.0079 | 0.0825 |
| seed_p_vs_seed_pars | 168 | -0.0081 | 0.0025 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
