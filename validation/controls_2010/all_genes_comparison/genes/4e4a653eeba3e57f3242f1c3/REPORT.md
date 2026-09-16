# YDL045C
Status: ok. Length: 1090 nt. Measured usable bases: 442. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 442 | 0.2907 | 0.2743 |
| rnafold | ok | 442 | 0.2552 | 0.2727 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.2774 | -0.3845 |
| seed_p | 46 | -0.6406 | -0.5586 |
| seed_p_vs_seed_pars | 33 | -0.6207 | -0.7941 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
