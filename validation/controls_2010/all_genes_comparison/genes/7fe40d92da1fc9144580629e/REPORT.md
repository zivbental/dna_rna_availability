# YGL224C
Status: ok. Length: 1058 nt. Measured usable bases: 467. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 467 | 0.2151 | 0.2199 |
| rnafold | ok | 467 | 0.2453 | 0.2488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.3261 | 0.2043 |
| seed_p | 67 | 0.4871 | 0.5001 |
| seed_p_vs_seed_pars | 38 | 0.4397 | 0.7366 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
