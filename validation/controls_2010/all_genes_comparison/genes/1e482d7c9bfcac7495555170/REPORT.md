# YCR027C
Status: ok. Length: 998 nt. Measured usable bases: 442. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 442 | 0.3332 | 0.3309 |
| rnafold | ok | 442 | 0.2665 | 0.2859 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | -0.7861 | -0.4616 |
| seed_p | 34 | -0.8607 | -0.7074 |
| seed_p_vs_seed_pars | 26 | -0.9696 | -0.9724 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
