# YJR135W-A
Status: ok. Length: 386 nt. Measured usable bases: 246. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 246 | 0.3216 | 0.3126 |
| rnafold | ok | 246 | 0.1861 | 0.2157 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 115 | -0.4665 | -0.2604 |
| seed_p | 115 | -0.4303 | -0.4010 |
| seed_p_vs_seed_pars | 89 | -0.4704 | -0.4095 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
