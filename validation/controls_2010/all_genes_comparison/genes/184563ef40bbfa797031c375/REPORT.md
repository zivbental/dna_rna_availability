# YBR146W
Status: ok. Length: 1103 nt. Measured usable bases: 643. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 643 | 0.3496 | 0.3483 |
| rnafold | ok | 643 | 0.2764 | 0.2846 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 224 | -0.0944 | -0.3099 |
| seed_p | 224 | -0.2856 | -0.3441 |
| seed_p_vs_seed_pars | 183 | -0.4118 | -0.4679 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
