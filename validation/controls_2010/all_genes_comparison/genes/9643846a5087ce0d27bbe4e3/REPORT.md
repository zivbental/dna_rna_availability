# YLR452C
Status: ok. Length: 2357 nt. Measured usable bases: 1450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1450 | 0.3050 | 0.2788 |
| rnafold | ok | 1450 | 0.2682 | 0.2467 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 596 | -0.0221 | -0.2099 |
| seed_p | 596 | -0.2291 | -0.1969 |
| seed_p_vs_seed_pars | 388 | -0.4500 | -0.3608 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
