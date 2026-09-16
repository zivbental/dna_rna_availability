# YHR132W-A
Status: ok. Length: 745 nt. Measured usable bases: 257. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 257 | 0.3808 | 0.3949 |
| rnafold | ok | 257 | 0.3462 | 0.3554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | 0.0171 | 0.0517 |
| seed_p | 54 | -0.2039 | 0.0815 |
| seed_p_vs_seed_pars | 43 | -0.3161 | -0.3580 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
