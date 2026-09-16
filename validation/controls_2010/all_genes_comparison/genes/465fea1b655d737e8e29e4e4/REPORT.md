# YGL111W
Status: ok. Length: 1563 nt. Measured usable bases: 719. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 719 | 0.3414 | 0.3389 |
| rnafold | ok | 719 | 0.2894 | 0.2999 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | 0.0152 | -0.3018 |
| seed_p | 97 | 0.0108 | -0.0399 |
| seed_p_vs_seed_pars | 64 | 0.1910 | -0.0588 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
