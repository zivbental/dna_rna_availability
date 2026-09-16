# YGR200C
Status: ok. Length: 2473 nt. Measured usable bases: 1271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1271 | 0.3268 | 0.3116 |
| rnafold | ok | 1271 | 0.2746 | 0.2933 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 373 | -0.1308 | -0.0873 |
| seed_p | 373 | -0.3636 | -0.2613 |
| seed_p_vs_seed_pars | 270 | -0.4434 | -0.3427 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
