# YGR245C
Status: ok. Length: 2480 nt. Measured usable bases: 889. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 889 | 0.3587 | 0.3722 |
| rnafold | ok | 889 | 0.3331 | 0.3562 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 104 | -0.0479 | -0.3530 |
| seed_p | 104 | -0.2149 | -0.3527 |
| seed_p_vs_seed_pars | 60 | 0.1012 | 0.2370 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
