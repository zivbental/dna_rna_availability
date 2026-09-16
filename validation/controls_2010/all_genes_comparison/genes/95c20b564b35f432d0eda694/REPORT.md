# YCR040W
Status: ok. Length: 528 nt. Measured usable bases: 352. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 352 | 0.2289 | 0.2394 |
| rnafold | ok | 352 | 0.2276 | 0.2406 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | -0.0502 | 0.0083 |
| seed_p | 208 | -0.1445 | -0.1438 |
| seed_p_vs_seed_pars | 155 | 0.0988 | 0.0992 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
