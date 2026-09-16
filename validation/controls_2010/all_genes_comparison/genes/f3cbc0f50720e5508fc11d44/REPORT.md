# YJR025C
Status: ok. Length: 729 nt. Measured usable bases: 355. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 355 | 0.4463 | 0.4505 |
| rnafold | ok | 355 | 0.3876 | 0.3865 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | -0.1419 | -0.6434 |
| seed_p | 107 | 0.3768 | 0.1596 |
| seed_p_vs_seed_pars | 63 | -0.0804 | -0.1062 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
