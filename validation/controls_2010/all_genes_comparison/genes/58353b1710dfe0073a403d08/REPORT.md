# YLR027C
Status: ok. Length: 1304 nt. Measured usable bases: 1176. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1176 | 0.3197 | 0.3043 |
| rnafold | ok | 1176 | 0.2530 | 0.2526 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1161 | -0.1244 | -0.0690 |
| seed_p | 1161 | -0.3685 | -0.2389 |
| seed_p_vs_seed_pars | 1074 | -0.4489 | -0.3499 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
