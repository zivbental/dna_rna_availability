# YDR116C
Status: ok. Length: 980 nt. Measured usable bases: 482. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 482 | 0.3896 | 0.3664 |
| rnafold | ok | 482 | 0.2713 | 0.2660 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.0788 | -0.2264 |
| seed_p | 77 | 0.0433 | -0.0238 |
| seed_p_vs_seed_pars | 60 | -0.1263 | -0.3002 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
