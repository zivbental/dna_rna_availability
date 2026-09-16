# YDR415C
Status: ok. Length: 1309 nt. Measured usable bases: 644. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 644 | 0.3480 | 0.3539 |
| rnafold | ok | 644 | 0.2183 | 0.2547 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 126 | -0.2196 | 0.1075 |
| seed_p | 126 | -0.1831 | -0.0467 |
| seed_p_vs_seed_pars | 77 | -0.4117 | -0.4069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
