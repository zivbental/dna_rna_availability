# YDR115W
Status: ok. Length: 439 nt. Measured usable bases: 234. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 234 | 0.0486 | 0.0530 |
| rnafold | ok | 234 | 0.1745 | 0.1555 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 69 | -0.0512 | -0.4081 |
| seed_p | 69 | 0.3196 | 0.4063 |
| seed_p_vs_seed_pars | 49 | 0.2208 | -0.0283 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
