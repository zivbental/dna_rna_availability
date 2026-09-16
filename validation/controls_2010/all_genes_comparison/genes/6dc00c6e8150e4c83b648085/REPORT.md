# YHR128W
Status: ok. Length: 932 nt. Measured usable bases: 757. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 757 | 0.3950 | 0.3819 |
| rnafold | ok | 757 | 0.2884 | 0.2958 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 640 | -0.2520 | -0.3109 |
| seed_p | 640 | -0.2866 | -0.2563 |
| seed_p_vs_seed_pars | 566 | -0.3719 | -0.3102 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
