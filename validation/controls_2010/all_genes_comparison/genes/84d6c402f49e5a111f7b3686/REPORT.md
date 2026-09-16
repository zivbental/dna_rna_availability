# YPL038W
Status: ok. Length: 660 nt. Measured usable bases: 308. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 308 | 0.4522 | 0.4531 |
| rnafold | ok | 308 | 0.4750 | 0.4700 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | 0.2623 | 0.1536 |
| seed_p | 63 | 0.0264 | -0.1094 |
| seed_p_vs_seed_pars | 40 | 0.0938 | -0.0580 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
