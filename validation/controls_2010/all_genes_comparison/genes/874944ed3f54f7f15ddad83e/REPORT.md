# YNL072W
Status: ok. Length: 1015 nt. Measured usable bases: 486. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 486 | 0.3319 | 0.3407 |
| rnafold | ok | 486 | 0.3469 | 0.3561 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | 0.1318 | -0.1041 |
| seed_p | 63 | -0.5211 | -0.5025 |
| seed_p_vs_seed_pars | 49 | -0.4159 | -0.5593 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
