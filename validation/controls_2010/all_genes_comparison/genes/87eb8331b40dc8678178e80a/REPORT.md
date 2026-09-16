# YER100W
Status: ok. Length: 1112 nt. Measured usable bases: 541. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 541 | 0.2601 | 0.2539 |
| rnafold | ok | 541 | 0.3046 | 0.3195 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 160 | -0.0816 | -0.0934 |
| seed_p | 160 | 0.0957 | 0.0354 |
| seed_p_vs_seed_pars | 106 | -0.2680 | -0.2713 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
