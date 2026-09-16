# YJL093C
Status: ok. Length: 2076 nt. Measured usable bases: 1064. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1064 | 0.2981 | 0.2799 |
| rnafold | ok | 1064 | 0.2150 | 0.1955 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | 0.0285 | -0.1130 |
| seed_p | 163 | -0.0774 | -0.1607 |
| seed_p_vs_seed_pars | 93 | 0.0133 | -0.0954 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
