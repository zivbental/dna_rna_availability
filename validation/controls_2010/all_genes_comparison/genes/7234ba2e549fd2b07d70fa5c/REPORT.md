# YKL098W
Status: ok. Length: 1195 nt. Measured usable bases: 491. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 491 | 0.3045 | 0.2979 |
| rnafold | ok | 491 | 0.1579 | 0.1532 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | -0.2834 | -0.7603 |
| seed_p | 42 | -0.5479 | -0.4548 |
| seed_p_vs_seed_pars | 31 | -0.5266 | -0.3583 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
