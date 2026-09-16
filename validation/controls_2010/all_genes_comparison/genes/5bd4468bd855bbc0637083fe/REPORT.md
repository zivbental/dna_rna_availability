# YER177W
Status: ok. Length: 1021 nt. Measured usable bases: 866. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 866 | 0.3415 | 0.3418 |
| rnafold | ok | 866 | 0.3364 | 0.3360 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 797 | -0.1573 | -0.3925 |
| seed_p | 797 | -0.3405 | -0.3838 |
| seed_p_vs_seed_pars | 728 | -0.4035 | -0.4051 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
