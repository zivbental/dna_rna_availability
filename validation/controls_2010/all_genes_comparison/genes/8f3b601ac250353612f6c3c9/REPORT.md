# YDR177W
Status: ok. Length: 795 nt. Measured usable bases: 477. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 477 | 0.1934 | 0.1900 |
| rnafold | ok | 477 | 0.1897 | 0.2039 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 274 | 0.2048 | 0.0534 |
| seed_p | 274 | 0.0131 | 0.0119 |
| seed_p_vs_seed_pars | 206 | -0.0494 | -0.0676 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
