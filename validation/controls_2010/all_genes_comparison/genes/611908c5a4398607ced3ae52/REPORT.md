# YKR043C
Status: ok. Length: 980 nt. Measured usable bases: 701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 701 | 0.3041 | 0.3037 |
| rnafold | ok | 701 | 0.3098 | 0.3102 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 527 | 0.0167 | -0.2381 |
| seed_p | 527 | -0.0119 | -0.1014 |
| seed_p_vs_seed_pars | 458 | -0.0630 | -0.0389 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
