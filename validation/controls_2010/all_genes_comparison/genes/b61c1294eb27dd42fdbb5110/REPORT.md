# YJR077C
Status: ok. Length: 1211 nt. Measured usable bases: 971. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 971 | 0.2851 | 0.2778 |
| rnafold | ok | 971 | 0.2436 | 0.2466 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 815 | -0.1804 | 0.0257 |
| seed_p | 815 | -0.1856 | -0.1073 |
| seed_p_vs_seed_pars | 714 | -0.2474 | -0.2023 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
