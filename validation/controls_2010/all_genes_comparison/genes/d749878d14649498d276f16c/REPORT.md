# YBL036C
Status: ok. Length: 924 nt. Measured usable bases: 419. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 419 | 0.5053 | 0.4968 |
| rnafold | ok | 419 | 0.4387 | 0.4425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.4607 | -0.5334 |
| seed_p | 46 | -0.7555 | -0.7447 |
| seed_p_vs_seed_pars | 36 | -0.5715 | -0.5164 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
