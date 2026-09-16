# YKR042W
Status: ok. Length: 1528 nt. Measured usable bases: 1287. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1287 | 0.2601 | 0.2505 |
| rnafold | ok | 1287 | 0.1632 | 0.1625 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1225 | -0.0746 | -0.2636 |
| seed_p | 1225 | -0.3002 | -0.3067 |
| seed_p_vs_seed_pars | 1128 | -0.2444 | -0.2401 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
