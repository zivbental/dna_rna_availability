# YPR033C
Status: ok. Length: 1688 nt. Measured usable bases: 1319. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1319 | 0.3501 | 0.3324 |
| rnafold | ok | 1319 | 0.2978 | 0.2839 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 993 | -0.2145 | -0.1532 |
| seed_p | 993 | -0.3496 | -0.2543 |
| seed_p_vs_seed_pars | 737 | -0.3427 | -0.3554 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
