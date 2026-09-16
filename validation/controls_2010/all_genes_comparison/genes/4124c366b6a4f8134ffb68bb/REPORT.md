# YBR252W
Status: ok. Length: 522 nt. Measured usable bases: 410. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 410 | 0.3740 | 0.3869 |
| rnafold | ok | 410 | 0.2913 | 0.3452 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 341 | 0.0051 | 0.1751 |
| seed_p | 341 | 0.1071 | 0.1314 |
| seed_p_vs_seed_pars | 276 | -0.2028 | -0.0768 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
