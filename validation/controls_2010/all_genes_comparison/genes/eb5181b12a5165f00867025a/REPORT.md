# YDR422C
Status: ok. Length: 2626 nt. Measured usable bases: 1008. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1008 | 0.3264 | 0.3194 |
| rnafold | ok | 1008 | 0.2782 | 0.2644 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | -0.1233 | 0.3146 |
| seed_p | 55 | 0.1924 | 0.2416 |
| seed_p_vs_seed_pars | 41 | -0.1594 | -0.0061 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
