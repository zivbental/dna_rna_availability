# YDR502C
Status: ok. Length: 1458 nt. Measured usable bases: 1089. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1089 | 0.3492 | 0.3398 |
| rnafold | ok | 1089 | 0.3152 | 0.3248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 820 | -0.0763 | -0.2041 |
| seed_p | 820 | -0.2999 | -0.3016 |
| seed_p_vs_seed_pars | 675 | -0.3038 | -0.3237 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
