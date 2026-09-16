# YKL080W
Status: ok. Length: 1301 nt. Measured usable bases: 1068. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1068 | 0.3224 | 0.3075 |
| rnafold | ok | 1068 | 0.2448 | 0.2436 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 985 | 0.0091 | 0.1043 |
| seed_p | 985 | -0.1768 | -0.0667 |
| seed_p_vs_seed_pars | 877 | -0.3675 | -0.3359 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
