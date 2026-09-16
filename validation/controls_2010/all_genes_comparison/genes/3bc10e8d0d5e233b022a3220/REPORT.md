# YJR064W
Status: ok. Length: 1782 nt. Measured usable bases: 1424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1424 | 0.3906 | 0.3808 |
| rnafold | ok | 1424 | 0.3000 | 0.3163 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1192 | -0.1289 | -0.1422 |
| seed_p | 1192 | -0.1580 | -0.1683 |
| seed_p_vs_seed_pars | 1059 | -0.4546 | -0.4042 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
