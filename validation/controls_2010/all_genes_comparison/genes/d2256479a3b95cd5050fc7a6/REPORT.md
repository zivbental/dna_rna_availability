# YBL072C
Status: ok. Length: 1003 nt. Measured usable bases: 221. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 221 | 0.4221 | 0.4309 |
| rnafold | ok | 221 | 0.4002 | 0.4265 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | -0.0925 | 0.1471 |
| seed_p | 88 | -0.1162 | -0.1646 |
| seed_p_vs_seed_pars | 86 | -0.2021 | -0.2149 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
