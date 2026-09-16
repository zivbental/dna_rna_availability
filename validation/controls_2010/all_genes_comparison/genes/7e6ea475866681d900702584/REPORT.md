# YDR111C
Status: ok. Length: 1751 nt. Measured usable bases: 733. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 733 | 0.2826 | 0.2696 |
| rnafold | ok | 733 | 0.2077 | 0.2180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | 0.2453 | -0.3682 |
| seed_p | 114 | 0.2345 | 0.0481 |
| seed_p_vs_seed_pars | 87 | 0.3386 | 0.1493 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
