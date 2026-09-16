# YOR108W
Status: ok. Length: 1998 nt. Measured usable bases: 1376. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1376 | 0.3283 | 0.3066 |
| rnafold | ok | 1376 | 0.2793 | 0.2617 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 828 | -0.0054 | 0.0078 |
| seed_p | 828 | -0.1325 | -0.0580 |
| seed_p_vs_seed_pars | 699 | -0.3616 | -0.3194 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
