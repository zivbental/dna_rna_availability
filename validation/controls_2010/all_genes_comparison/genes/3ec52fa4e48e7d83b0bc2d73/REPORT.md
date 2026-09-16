# YEL032W
Status: ok. Length: 3109 nt. Measured usable bases: 1725. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1725 | 0.3032 | 0.2947 |
| rnafold | ok | 1725 | 0.2424 | 0.2309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 508 | -0.1510 | -0.2542 |
| seed_p | 508 | -0.3193 | -0.3923 |
| seed_p_vs_seed_pars | 381 | -0.2871 | -0.2756 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
