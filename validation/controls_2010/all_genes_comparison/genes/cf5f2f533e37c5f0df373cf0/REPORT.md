# YPL206C
Status: ok. Length: 1116 nt. Measured usable bases: 613. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 613 | 0.2716 | 0.2679 |
| rnafold | ok | 613 | 0.1449 | 0.1488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 279 | -0.0710 | -0.0740 |
| seed_p | 279 | -0.2213 | -0.1055 |
| seed_p_vs_seed_pars | 219 | -0.3092 | -0.1711 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
