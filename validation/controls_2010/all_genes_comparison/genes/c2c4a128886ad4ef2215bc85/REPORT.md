# YBR031W
Status: ok. Length: 1353 nt. Measured usable bases: 198. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 198 | 0.3440 | 0.3038 |
| rnafold | ok | 198 | 0.2824 | 0.2783 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | -0.0408 | -0.2752 |
| seed_p | 94 | -0.3113 | -0.1199 |
| seed_p_vs_seed_pars | 85 | -0.1835 | 0.1004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
