# YML074C
Status: ok. Length: 1361 nt. Measured usable bases: 787. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 787 | 0.3262 | 0.3295 |
| rnafold | ok | 787 | 0.3500 | 0.3312 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 476 | -0.1787 | -0.0028 |
| seed_p | 476 | -0.2473 | -0.1860 |
| seed_p_vs_seed_pars | 351 | -0.5050 | -0.3851 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
