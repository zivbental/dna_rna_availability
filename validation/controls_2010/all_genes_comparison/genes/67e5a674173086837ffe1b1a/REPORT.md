# YNL248C
Status: ok. Length: 1483 nt. Measured usable bases: 926. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 926 | 0.3303 | 0.3121 |
| rnafold | ok | 926 | 0.2313 | 0.2323 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 477 | -0.1257 | -0.3958 |
| seed_p | 477 | -0.4182 | -0.4545 |
| seed_p_vs_seed_pars | 362 | -0.5186 | -0.5735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
