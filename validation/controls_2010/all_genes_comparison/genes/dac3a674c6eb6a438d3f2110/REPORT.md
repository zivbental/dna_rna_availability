# YNL182C
Status: ok. Length: 1794 nt. Measured usable bases: 1012. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1012 | 0.3665 | 0.3601 |
| rnafold | ok | 1012 | 0.3045 | 0.3056 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 285 | -0.2621 | -0.2059 |
| seed_p | 285 | -0.2536 | -0.1621 |
| seed_p_vs_seed_pars | 215 | -0.2415 | -0.1723 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
