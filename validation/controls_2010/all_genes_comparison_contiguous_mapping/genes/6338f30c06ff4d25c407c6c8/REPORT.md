# YBL041W
Status: ok. Length: 816 nt. Measured usable bases: 612.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.3046 | 0.2937 |
| rnafold | ok | 612 | 0.1843 | 0.1898 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 489 | -0.3234 | -0.4112 |
| seed_p | 489 | -0.4599 | -0.4280 |
| seed_p_vs_seed_pars | 377 | -0.4353 | -0.4812 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
