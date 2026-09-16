# YPL098C
Status: ok. Length: 510 nt. Measured usable bases: 375. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 375 | 0.2766 | 0.2880 |
| rnafold | ok | 375 | 0.2417 | 0.2772 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 288 | 0.0912 | -0.1114 |
| seed_p | 288 | 0.0949 | -0.0240 |
| seed_p_vs_seed_pars | 243 | 0.1613 | 0.1200 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
