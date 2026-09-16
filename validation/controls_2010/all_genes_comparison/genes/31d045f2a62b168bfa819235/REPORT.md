# YGL161C
Status: ok. Length: 1160 nt. Measured usable bases: 863. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 863 | 0.2809 | 0.2740 |
| rnafold | ok | 863 | 0.2853 | 0.2942 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 595 | -0.0962 | 0.1741 |
| seed_p | 595 | 0.0048 | -0.0223 |
| seed_p_vs_seed_pars | 456 | -0.2023 | -0.2703 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
