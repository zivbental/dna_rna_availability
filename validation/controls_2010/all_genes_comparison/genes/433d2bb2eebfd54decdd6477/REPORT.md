# YDR477W
Status: ok. Length: 2285 nt. Measured usable bases: 1050. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1050 | 0.2964 | 0.2932 |
| rnafold | ok | 1050 | 0.2679 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 184 | -0.0714 | 0.0381 |
| seed_p | 184 | -0.1633 | -0.2210 |
| seed_p_vs_seed_pars | 113 | -0.0612 | -0.0483 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
