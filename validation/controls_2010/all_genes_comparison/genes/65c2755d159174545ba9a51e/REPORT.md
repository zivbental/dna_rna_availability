# YDL128W
Status: ok. Length: 1500 nt. Measured usable bases: 1087. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1087 | 0.2437 | 0.2260 |
| rnafold | ok | 1087 | 0.1780 | 0.1941 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 753 | 0.0083 | 0.1049 |
| seed_p | 753 | -0.0303 | 0.0993 |
| seed_p_vs_seed_pars | 600 | -0.1441 | -0.0263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
