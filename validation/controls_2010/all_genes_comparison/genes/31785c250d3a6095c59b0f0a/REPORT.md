# YNL177C
Status: ok. Length: 1122 nt. Measured usable bases: 442. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 442 | 0.3569 | 0.3517 |
| rnafold | ok | 442 | 0.3185 | 0.3386 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | 0.1536 | -0.0006 |
| seed_p | 71 | -0.0090 | -0.0454 |
| seed_p_vs_seed_pars | 64 | 0.2269 | -0.0027 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
