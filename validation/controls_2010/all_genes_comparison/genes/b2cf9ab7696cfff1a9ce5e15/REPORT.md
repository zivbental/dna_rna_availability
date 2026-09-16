# YIL083C
Status: ok. Length: 1284 nt. Measured usable bases: 685. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 685 | 0.2674 | 0.2693 |
| rnafold | ok | 685 | 0.2138 | 0.2269 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 207 | 0.0527 | 0.1246 |
| seed_p | 207 | -0.1024 | -0.0864 |
| seed_p_vs_seed_pars | 146 | -0.4722 | -0.3435 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
