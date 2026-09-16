# YML102W
Status: ok. Length: 1570 nt. Measured usable bases: 756. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 756 | 0.3626 | 0.3575 |
| rnafold | ok | 756 | 0.2943 | 0.2997 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | 0.0446 | 0.1662 |
| seed_p | 110 | 0.1305 | 0.2013 |
| seed_p_vs_seed_pars | 63 | -0.3510 | -0.3648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
