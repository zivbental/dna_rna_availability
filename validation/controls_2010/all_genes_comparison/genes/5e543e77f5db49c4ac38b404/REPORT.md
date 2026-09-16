# YLR418C
Status: ok. Length: 1532 nt. Measured usable bases: 744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 744 | 0.3151 | 0.3016 |
| rnafold | ok | 744 | 0.2484 | 0.2584 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | -0.0030 | 0.0077 |
| seed_p | 72 | -0.1153 | -0.1366 |
| seed_p_vs_seed_pars | 58 | -0.2494 | -0.2988 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
