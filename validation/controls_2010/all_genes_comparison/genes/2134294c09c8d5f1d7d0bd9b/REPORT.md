# YDR028C
Status: ok. Length: 3620 nt. Measured usable bases: 1493. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1493 | 0.3268 | 0.3259 |
| rnafold | ok | 1493 | 0.2962 | 0.2956 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 142 | -0.0287 | 0.0700 |
| seed_p | 142 | -0.0431 | 0.0325 |
| seed_p_vs_seed_pars | 90 | -0.1289 | -0.0754 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
