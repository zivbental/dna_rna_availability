# YKL163W
Status: ok. Length: 1600 nt. Measured usable bases: 324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 324 | 0.3726 | 0.4009 |
| rnafold | ok | 324 | 0.3435 | 0.3648 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 6 | undefined | undefined |
| seed_p | 6 | undefined | undefined |
| seed_p_vs_seed_pars | 5 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
