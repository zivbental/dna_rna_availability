# YDR429C
Status: ok. Length: 921 nt. Measured usable bases: 686. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 686 | 0.3450 | 0.3360 |
| rnafold | ok | 686 | 0.3071 | 0.3116 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 501 | -0.1996 | -0.2483 |
| seed_p | 501 | -0.3949 | -0.3051 |
| seed_p_vs_seed_pars | 399 | -0.4481 | -0.3308 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
