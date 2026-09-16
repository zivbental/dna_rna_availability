# YBR267W
Status: ok. Length: 1309 nt. Measured usable bases: 633. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 633 | 0.4188 | 0.4124 |
| rnafold | ok | 633 | 0.3978 | 0.3930 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | -0.2060 | -0.4195 |
| seed_p | 110 | -0.1041 | -0.1540 |
| seed_p_vs_seed_pars | 74 | 0.0281 | -0.0374 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
