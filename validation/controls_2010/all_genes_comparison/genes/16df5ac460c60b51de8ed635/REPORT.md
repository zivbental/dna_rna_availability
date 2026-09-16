# YHR136C
Status: ok. Length: 613 nt. Measured usable bases: 314. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 314 | 0.3061 | 0.3105 |
| rnafold | ok | 314 | 0.1787 | 0.1784 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 206 | -0.3045 | -0.3063 |
| seed_p | 206 | -0.4050 | -0.3028 |
| seed_p_vs_seed_pars | 152 | -0.3323 | -0.3557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
