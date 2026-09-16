# YHR047C
Status: ok. Length: 2743 nt. Measured usable bases: 1745. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1745 | 0.3206 | 0.3076 |
| rnafold | ok | 1745 | 0.2681 | 0.2644 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 779 | 0.1094 | -0.0275 |
| seed_p | 779 | -0.2330 | -0.1326 |
| seed_p_vs_seed_pars | 543 | -0.2513 | -0.1602 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
