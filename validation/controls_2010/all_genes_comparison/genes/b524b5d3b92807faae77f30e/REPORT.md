# YOR292C
Status: ok. Length: 987 nt. Measured usable bases: 420. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 420 | 0.2361 | 0.2085 |
| rnafold | ok | 420 | 0.1658 | 0.1419 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 78 | 0.2366 | -0.3429 |
| seed_p | 78 | 0.4001 | 0.1256 |
| seed_p_vs_seed_pars | 56 | 0.5446 | 0.2843 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
