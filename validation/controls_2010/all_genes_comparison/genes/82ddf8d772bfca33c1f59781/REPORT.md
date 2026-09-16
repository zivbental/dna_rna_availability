# YLR186W
Status: ok. Length: 883 nt. Measured usable bases: 675. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 675 | 0.3898 | 0.3660 |
| rnafold | ok | 675 | 0.3317 | 0.3250 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 531 | -0.0031 | -0.1582 |
| seed_p | 531 | -0.4695 | -0.3159 |
| seed_p_vs_seed_pars | 439 | -0.6691 | -0.6178 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
