# YER099C
Status: ok. Length: 1281 nt. Measured usable bases: 572. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 572 | 0.2791 | 0.2614 |
| rnafold | ok | 572 | 0.1971 | 0.1862 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.2775 | -0.4316 |
| seed_p | 166 | 0.2725 | 0.1770 |
| seed_p_vs_seed_pars | 107 | 0.4092 | 0.3640 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
