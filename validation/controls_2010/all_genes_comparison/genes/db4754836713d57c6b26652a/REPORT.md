# YDL168W
Status: ok. Length: 1277 nt. Measured usable bases: 852. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 852 | 0.4130 | 0.3914 |
| rnafold | ok | 852 | 0.2721 | 0.2802 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 413 | -0.3707 | -0.3096 |
| seed_p | 413 | -0.3245 | -0.2317 |
| seed_p_vs_seed_pars | 339 | -0.2873 | -0.2803 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
