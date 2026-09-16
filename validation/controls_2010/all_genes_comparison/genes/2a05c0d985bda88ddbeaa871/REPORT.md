# YCR052W
Status: ok. Length: 1683 nt. Measured usable bases: 982. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 982 | 0.3517 | 0.3345 |
| rnafold | ok | 982 | 0.3496 | 0.3384 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 437 | -0.1602 | -0.1059 |
| seed_p | 437 | -0.3597 | -0.2824 |
| seed_p_vs_seed_pars | 364 | -0.4315 | -0.3845 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
