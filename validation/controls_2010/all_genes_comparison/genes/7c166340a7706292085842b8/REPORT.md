# YML120C
Status: ok. Length: 1933 nt. Measured usable bases: 733. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 733 | 0.3698 | 0.3561 |
| rnafold | ok | 733 | 0.3090 | 0.2977 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | 0.2163 | -0.1054 |
| seed_p | 82 | -0.5421 | -0.5317 |
| seed_p_vs_seed_pars | 49 | -0.7531 | -0.5166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
