# YBR248C
Status: ok. Length: 1790 nt. Measured usable bases: 935. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 935 | 0.3543 | 0.3562 |
| rnafold | ok | 935 | 0.2991 | 0.3084 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.0191 | -0.0459 |
| seed_p | 293 | 0.1493 | 0.2559 |
| seed_p_vs_seed_pars | 210 | 0.0497 | 0.2032 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
