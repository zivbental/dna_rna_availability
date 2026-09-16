# YDR170C
Status: ok. Length: 6476 nt. Measured usable bases: 2892. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2892 | 0.3172 | 0.3038 |
| rnafold | ok | 2892 | 0.2470 | 0.2302 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 560 | 0.1114 | -0.0526 |
| seed_p | 560 | 0.1088 | 0.0403 |
| seed_p_vs_seed_pars | 398 | 0.1537 | 0.0607 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
