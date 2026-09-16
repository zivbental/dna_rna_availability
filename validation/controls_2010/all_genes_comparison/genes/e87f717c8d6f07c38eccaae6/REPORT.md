# YCR034W
Status: ok. Length: 1240 nt. Measured usable bases: 954. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 954 | 0.2707 | 0.2566 |
| rnafold | ok | 954 | 0.2260 | 0.2152 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 782 | -0.0680 | 0.0414 |
| seed_p | 782 | -0.1500 | -0.1376 |
| seed_p_vs_seed_pars | 604 | -0.2684 | -0.2859 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
