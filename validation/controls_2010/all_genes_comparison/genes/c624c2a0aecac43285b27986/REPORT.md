# YKL103C
Status: ok. Length: 1763 nt. Measured usable bases: 701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 701 | 0.3395 | 0.3126 |
| rnafold | ok | 701 | 0.2960 | 0.2624 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 100 | -0.1441 | 0.0098 |
| seed_p | 100 | -0.4234 | -0.3372 |
| seed_p_vs_seed_pars | 88 | -0.5512 | -0.4038 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
