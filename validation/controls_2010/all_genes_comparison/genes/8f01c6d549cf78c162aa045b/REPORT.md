# YKR092C
Status: ok. Length: 1369 nt. Measured usable bases: 807. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 807 | 0.2668 | 0.2559 |
| rnafold | ok | 807 | 0.2157 | 0.2015 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 398 | -0.4586 | -0.2894 |
| seed_p | 398 | -0.4216 | -0.3016 |
| seed_p_vs_seed_pars | 328 | -0.4303 | -0.4475 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
