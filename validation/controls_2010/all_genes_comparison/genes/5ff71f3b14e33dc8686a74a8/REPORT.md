# YFL001W
Status: ok. Length: 1370 nt. Measured usable bases: 534. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 534 | 0.2533 | 0.2463 |
| rnafold | ok | 534 | 0.1427 | 0.1330 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 47 | -0.0280 | -0.0168 |
| seed_p | 47 | -0.5840 | -0.1807 |
| seed_p_vs_seed_pars | 34 | -0.8065 | -0.4260 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
