# YDL076C
Status: ok. Length: 1178 nt. Measured usable bases: 472. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 472 | 0.3177 | 0.3066 |
| rnafold | ok | 472 | 0.2700 | 0.2586 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | 0.0608 | 0.3049 |
| seed_p | 50 | -0.0064 | 0.1359 |
| seed_p_vs_seed_pars | 35 | 0.0939 | 0.0696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
