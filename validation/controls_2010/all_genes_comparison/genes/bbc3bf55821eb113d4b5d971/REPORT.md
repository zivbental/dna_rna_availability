# YKL214C
Status: ok. Length: 708 nt. Measured usable bases: 320. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 320 | 0.4440 | 0.4499 |
| rnafold | ok | 320 | 0.3800 | 0.4067 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | 0.0049 | 0.0366 |
| seed_p | 55 | -0.4226 | -0.0934 |
| seed_p_vs_seed_pars | 22 | 0.3100 | 0.6780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
