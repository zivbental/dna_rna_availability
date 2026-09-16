# YPL224C
Status: ok. Length: 1795 nt. Measured usable bases: 781. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 781 | 0.3373 | 0.3204 |
| rnafold | ok | 781 | 0.3034 | 0.2913 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | -0.1001 | -0.2964 |
| seed_p | 123 | -0.0869 | -0.0151 |
| seed_p_vs_seed_pars | 98 | -0.3899 | -0.3282 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
