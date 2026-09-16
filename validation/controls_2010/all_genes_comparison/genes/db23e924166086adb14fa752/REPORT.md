# YLR060W
Status: ok. Length: 2082 nt. Measured usable bases: 1626. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1626 | 0.2951 | 0.2837 |
| rnafold | ok | 1626 | 0.2463 | 0.2567 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1421 | -0.0493 | 0.0330 |
| seed_p | 1421 | -0.1240 | -0.0272 |
| seed_p_vs_seed_pars | 1222 | -0.2951 | -0.1557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
