# YJR014W
Status: ok. Length: 736 nt. Measured usable bases: 458. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 458 | 0.4005 | 0.3922 |
| rnafold | ok | 458 | 0.3231 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 186 | -0.0018 | -0.4252 |
| seed_p | 186 | -0.3689 | -0.3880 |
| seed_p_vs_seed_pars | 145 | -0.2853 | -0.2727 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
