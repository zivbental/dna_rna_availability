# YER044C
Status: ok. Length: 619 nt. Measured usable bases: 387. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 387 | 0.2944 | 0.2571 |
| rnafold | ok | 387 | 0.1850 | 0.1412 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 181 | -0.6389 | -0.4464 |
| seed_p | 181 | -0.2917 | -0.1357 |
| seed_p_vs_seed_pars | 152 | -0.4858 | -0.3858 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
