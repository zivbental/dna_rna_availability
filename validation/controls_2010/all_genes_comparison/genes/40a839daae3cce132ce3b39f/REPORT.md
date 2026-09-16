# YIR018W
Status: ok. Length: 904 nt. Measured usable bases: 417. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 417 | 0.3491 | 0.3298 |
| rnafold | ok | 417 | 0.2927 | 0.2777 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | 0.0807 | 0.2176 |
| seed_p | 53 | 0.1261 | 0.0391 |
| seed_p_vs_seed_pars | 34 | -0.4758 | -0.5013 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
