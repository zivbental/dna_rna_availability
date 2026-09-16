# YDL208W
Status: ok. Length: 625 nt. Measured usable bases: 427. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 427 | 0.2905 | 0.2922 |
| rnafold | ok | 427 | 0.2472 | 0.2401 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 276 | 0.0847 | 0.0275 |
| seed_p | 276 | 0.0665 | 0.0230 |
| seed_p_vs_seed_pars | 210 | 0.0537 | 0.0991 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
