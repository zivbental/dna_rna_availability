# YNL023C
Status: ok. Length: 3111 nt. Measured usable bases: 1228. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1228 | 0.4095 | 0.3982 |
| rnafold | ok | 1228 | 0.3587 | 0.3559 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.2158 | -0.3745 |
| seed_p | 84 | 0.2396 | 0.1699 |
| seed_p_vs_seed_pars | 76 | 0.3553 | 0.4263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
