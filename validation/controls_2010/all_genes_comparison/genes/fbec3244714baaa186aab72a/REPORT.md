# YCR039C
Status: ok. Length: 633 nt. Measured usable bases: 286. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 286 | 0.3326 | 0.3321 |
| rnafold | ok | 286 | 0.3722 | 0.3756 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | 0.3712 | 0.1429 |
| seed_p | 60 | -0.0005 | 0.0886 |
| seed_p_vs_seed_pars | 48 | -0.3581 | -0.1891 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
