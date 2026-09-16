# YDR161W
Status: ok. Length: 1282 nt. Measured usable bases: 746. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 746 | 0.4011 | 0.3729 |
| rnafold | ok | 746 | 0.3667 | 0.3463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 232 | 0.2387 | 0.2518 |
| seed_p | 232 | 0.0110 | -0.0615 |
| seed_p_vs_seed_pars | 170 | -0.0790 | 0.0024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
