# YKL186C
Status: ok. Length: 999 nt. Measured usable bases: 528. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 528 | 0.3063 | 0.3073 |
| rnafold | ok | 528 | 0.2952 | 0.3225 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 258 | -0.2694 | -0.3755 |
| seed_p | 258 | -0.3654 | -0.3748 |
| seed_p_vs_seed_pars | 213 | -0.6297 | -0.6402 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
