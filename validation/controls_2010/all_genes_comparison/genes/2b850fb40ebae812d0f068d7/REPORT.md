# YMR006C
Status: ok. Length: 2286 nt. Measured usable bases: 1726. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1726 | 0.2923 | 0.2754 |
| rnafold | ok | 1726 | 0.1734 | 0.1579 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1230 | 0.0398 | -0.0028 |
| seed_p | 1230 | 0.0185 | 0.0446 |
| seed_p_vs_seed_pars | 931 | -0.1218 | -0.0332 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
