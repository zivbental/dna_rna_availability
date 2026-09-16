# YDR321W
Status: ok. Length: 1263 nt. Measured usable bases: 1066. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1066 | 0.3381 | 0.3136 |
| rnafold | ok | 1066 | 0.2807 | 0.2610 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 998 | 0.0308 | -0.0528 |
| seed_p | 998 | -0.0965 | -0.0697 |
| seed_p_vs_seed_pars | 871 | -0.1999 | -0.2039 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
