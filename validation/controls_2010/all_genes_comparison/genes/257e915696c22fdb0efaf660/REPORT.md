# YPL117C
Status: ok. Length: 1126 nt. Measured usable bases: 727. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 727 | 0.3010 | 0.3010 |
| rnafold | ok | 727 | 0.2504 | 0.2607 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 428 | 0.0967 | 0.2243 |
| seed_p | 428 | 0.1535 | 0.2237 |
| seed_p_vs_seed_pars | 358 | 0.1040 | 0.1047 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
