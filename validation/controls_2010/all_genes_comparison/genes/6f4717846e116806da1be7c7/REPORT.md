# YCL040W
Status: ok. Length: 1714 nt. Measured usable bases: 526. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 526 | 0.3028 | 0.2641 |
| rnafold | ok | 526 | 0.3295 | 0.3016 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 468 | 0.0354 | -0.0653 |
| seed_p | 468 | -0.1377 | -0.1752 |
| seed_p_vs_seed_pars | 392 | -0.1896 | -0.2612 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
