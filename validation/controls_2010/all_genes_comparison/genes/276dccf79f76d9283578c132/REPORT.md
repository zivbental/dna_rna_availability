# YBL093C
Status: ok. Length: 905 nt. Measured usable bases: 499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.3736 | 0.3748 |
| rnafold | ok | 499 | 0.3189 | 0.3159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | 0.1427 | 0.0165 |
| seed_p | 159 | 0.1500 | 0.1569 |
| seed_p_vs_seed_pars | 127 | 0.1290 | 0.0437 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
