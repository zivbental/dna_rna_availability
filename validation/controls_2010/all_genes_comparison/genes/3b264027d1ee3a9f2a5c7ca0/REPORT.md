# YLR354C
Status: ok. Length: 1147 nt. Measured usable bases: 1023. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1023 | 0.3657 | 0.3512 |
| rnafold | ok | 1023 | 0.2736 | 0.2672 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1023 | -0.0503 | -0.1095 |
| seed_p | 1023 | -0.1428 | -0.1933 |
| seed_p_vs_seed_pars | 950 | -0.2920 | -0.2388 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
