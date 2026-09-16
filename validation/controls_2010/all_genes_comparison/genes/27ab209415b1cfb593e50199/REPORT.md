# YLR147C
Status: ok. Length: 417 nt. Measured usable bases: 188. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 188 | 0.3645 | 0.3202 |
| rnafold | ok | 188 | 0.2966 | 0.2700 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | -0.1451 | -0.4573 |
| seed_p | 93 | -0.4036 | -0.3814 |
| seed_p_vs_seed_pars | 67 | -0.7986 | -0.8012 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
