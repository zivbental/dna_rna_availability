# YPL265W
Status: ok. Length: 2203 nt. Measured usable bases: 1298. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1298 | 0.2208 | 0.1971 |
| rnafold | ok | 1298 | 0.1999 | 0.1760 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 504 | 0.1202 | 0.0609 |
| seed_p | 504 | -0.1061 | -0.0253 |
| seed_p_vs_seed_pars | 374 | -0.2152 | -0.1595 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
