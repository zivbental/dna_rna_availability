# YKL046C
Status: ok. Length: 1609 nt. Measured usable bases: 1186. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1186 | 0.2733 | 0.2360 |
| rnafold | ok | 1186 | 0.2295 | 0.2110 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 821 | -0.0419 | 0.0216 |
| seed_p | 821 | 0.0327 | 0.0797 |
| seed_p_vs_seed_pars | 606 | 0.0078 | 0.0474 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
