# YLR207W
Status: ok. Length: 2601 nt. Measured usable bases: 942. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 942 | 0.3774 | 0.3740 |
| rnafold | ok | 942 | 0.3016 | 0.3042 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.3654 | -0.3136 |
| seed_p | 43 | -0.1914 | -0.3071 |
| seed_p_vs_seed_pars | 36 | -0.0514 | 0.1001 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
