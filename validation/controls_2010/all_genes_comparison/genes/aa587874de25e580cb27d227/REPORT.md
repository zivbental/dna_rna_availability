# YDL084W
Status: ok. Length: 1608 nt. Measured usable bases: 1405. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1405 | 0.3027 | 0.2851 |
| rnafold | ok | 1405 | 0.2259 | 0.2149 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1354 | -0.1745 | -0.1129 |
| seed_p | 1354 | -0.1490 | -0.0832 |
| seed_p_vs_seed_pars | 1248 | -0.2816 | -0.3007 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
