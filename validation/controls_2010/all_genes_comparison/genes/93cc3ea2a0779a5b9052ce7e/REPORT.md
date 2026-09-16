# YLR356W
Status: ok. Length: 750 nt. Measured usable bases: 335. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 335 | 0.3103 | 0.3044 |
| rnafold | ok | 335 | 0.2663 | 0.2615 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.3113 | 0.1980 |
| seed_p | 58 | -0.6385 | -0.3828 |
| seed_p_vs_seed_pars | 47 | -0.8315 | -0.7162 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
