# YMR139W
Status: ok. Length: 1422 nt. Measured usable bases: 641. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 641 | 0.2703 | 0.2650 |
| rnafold | ok | 641 | 0.2111 | 0.1985 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.2465 | 0.0339 |
| seed_p | 87 | 0.7579 | 0.7278 |
| seed_p_vs_seed_pars | 67 | 0.7144 | 0.5521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
