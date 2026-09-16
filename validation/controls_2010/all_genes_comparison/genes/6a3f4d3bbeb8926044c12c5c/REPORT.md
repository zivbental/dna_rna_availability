# YHR088W
Status: ok. Length: 1013 nt. Measured usable bases: 380. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 380 | 0.2666 | 0.2649 |
| rnafold | ok | 380 | 0.2770 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | -0.7972 | -0.7825 |
| seed_p | 26 | -0.6356 | -0.5702 |
| seed_p_vs_seed_pars | 12 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
