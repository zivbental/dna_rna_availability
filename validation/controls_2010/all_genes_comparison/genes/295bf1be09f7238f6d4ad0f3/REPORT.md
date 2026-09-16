# YKL160W
Status: ok. Length: 527 nt. Measured usable bases: 346. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 346 | 0.3861 | 0.4161 |
| rnafold | ok | 346 | 0.3372 | 0.3538 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 194 | -0.3475 | -0.1586 |
| seed_p | 194 | -0.2545 | -0.1386 |
| seed_p_vs_seed_pars | 105 | -0.1945 | -0.0530 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
