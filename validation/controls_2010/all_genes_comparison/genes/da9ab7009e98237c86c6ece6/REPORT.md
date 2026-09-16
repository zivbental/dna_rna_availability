# YDL081C
Status: ok. Length: 452 nt. Measured usable bases: 373. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 373 | 0.2593 | 0.2759 |
| rnafold | ok | 373 | 0.1417 | 0.1799 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 323 | -0.1999 | -0.1710 |
| seed_p | 323 | -0.2664 | -0.3122 |
| seed_p_vs_seed_pars | 292 | -0.2332 | -0.2124 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
