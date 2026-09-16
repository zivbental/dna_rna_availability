# YDL134C
Status: ok. Length: 1625 nt. Measured usable bases: 893. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 893 | 0.2941 | 0.2820 |
| rnafold | ok | 893 | 0.2877 | 0.2854 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 383 | 0.1825 | 0.1373 |
| seed_p | 383 | -0.0302 | -0.0157 |
| seed_p_vs_seed_pars | 280 | -0.1279 | -0.1313 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
