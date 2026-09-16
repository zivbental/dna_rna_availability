# YDL093W
Status: ok. Length: 2500 nt. Measured usable bases: 1134. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1134 | 0.2925 | 0.2778 |
| rnafold | ok | 1134 | 0.2654 | 0.2575 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | 0.0188 | -0.0370 |
| seed_p | 126 | 0.0354 | 0.0089 |
| seed_p_vs_seed_pars | 88 | 0.0291 | -0.0995 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
