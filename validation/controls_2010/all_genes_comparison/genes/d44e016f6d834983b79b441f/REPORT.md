# YNL320W
Status: ok. Length: 1019 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.2886 | 0.2805 |
| rnafold | ok | 533 | 0.2574 | 0.2522 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 150 | 0.1412 | -0.0015 |
| seed_p | 150 | -0.1441 | -0.0756 |
| seed_p_vs_seed_pars | 104 | -0.2863 | -0.1870 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
