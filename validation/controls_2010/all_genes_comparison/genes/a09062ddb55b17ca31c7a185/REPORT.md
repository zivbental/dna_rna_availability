# YOL147C
Status: ok. Length: 911 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.1951 | 0.2235 |
| rnafold | ok | 444 | 0.1917 | 0.2335 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | 0.1800 | 0.3559 |
| seed_p | 174 | -0.0250 | -0.0280 |
| seed_p_vs_seed_pars | 115 | -0.4482 | -0.3743 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
