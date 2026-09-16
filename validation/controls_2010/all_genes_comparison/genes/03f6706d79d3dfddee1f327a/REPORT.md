# YOR168W
Status: ok. Length: 2531 nt. Measured usable bases: 1955. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1955 | 0.3525 | 0.3458 |
| rnafold | ok | 1955 | 0.3580 | 0.3435 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1446 | -0.1683 | -0.2241 |
| seed_p | 1446 | -0.1369 | -0.1438 |
| seed_p_vs_seed_pars | 1143 | -0.1849 | -0.2200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
