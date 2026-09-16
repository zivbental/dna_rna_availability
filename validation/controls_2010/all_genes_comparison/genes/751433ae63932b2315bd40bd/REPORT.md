# YER168C
Status: ok. Length: 1723 nt. Measured usable bases: 763. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 763 | 0.3871 | 0.3639 |
| rnafold | ok | 763 | 0.2441 | 0.2433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | 0.0049 | -0.3808 |
| seed_p | 90 | 0.1370 | -0.0714 |
| seed_p_vs_seed_pars | 63 | -0.0107 | -0.0277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
