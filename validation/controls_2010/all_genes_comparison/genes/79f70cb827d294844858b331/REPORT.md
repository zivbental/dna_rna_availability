# YOL082W
Status: ok. Length: 1461 nt. Measured usable bases: 637. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 637 | 0.3534 | 0.3331 |
| rnafold | ok | 637 | 0.2978 | 0.2757 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.4161 | -0.5192 |
| seed_p | 40 | -0.7583 | -0.7875 |
| seed_p_vs_seed_pars | 32 | -0.7501 | -0.7378 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
