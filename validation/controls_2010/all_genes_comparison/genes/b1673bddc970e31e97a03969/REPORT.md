# YHR051W
Status: ok. Length: 951 nt. Measured usable bases: 510. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 510 | 0.2462 | 0.2337 |
| rnafold | ok | 510 | 0.1684 | 0.1514 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 268 | -0.1116 | -0.1663 |
| seed_p | 268 | -0.2990 | -0.3620 |
| seed_p_vs_seed_pars | 205 | -0.2685 | -0.3986 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
