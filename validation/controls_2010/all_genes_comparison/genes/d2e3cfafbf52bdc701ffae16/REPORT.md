# YLR231C
Status: ok. Length: 1472 nt. Measured usable bases: 971. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 971 | 0.3148 | 0.3190 |
| rnafold | ok | 971 | 0.2365 | 0.2595 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 397 | 0.0512 | -0.2672 |
| seed_p | 397 | -0.1019 | -0.1298 |
| seed_p_vs_seed_pars | 295 | -0.1621 | -0.1647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
