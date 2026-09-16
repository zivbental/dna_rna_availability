# YDR272W
Status: ok. Length: 921 nt. Measured usable bases: 502. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 502 | 0.4421 | 0.4268 |
| rnafold | ok | 502 | 0.3640 | 0.3808 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | -0.2724 | -0.2853 |
| seed_p | 141 | 0.0263 | 0.1889 |
| seed_p_vs_seed_pars | 114 | 0.0920 | 0.0342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
