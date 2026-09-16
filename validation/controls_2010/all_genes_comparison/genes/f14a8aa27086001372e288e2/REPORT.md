# YLR380W
Status: ok. Length: 1440 nt. Measured usable bases: 928. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 928 | 0.2937 | 0.2913 |
| rnafold | ok | 928 | 0.2020 | 0.2025 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 515 | 0.0105 | -0.0045 |
| seed_p | 515 | -0.0820 | -0.0573 |
| seed_p_vs_seed_pars | 429 | -0.1066 | -0.0575 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
