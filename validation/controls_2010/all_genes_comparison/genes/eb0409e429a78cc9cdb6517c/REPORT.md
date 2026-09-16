# YOR362C
Status: ok. Length: 1024 nt. Measured usable bases: 835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 835 | 0.4394 | 0.4407 |
| rnafold | ok | 835 | 0.3525 | 0.3574 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 730 | -0.1402 | -0.1182 |
| seed_p | 730 | -0.1235 | -0.1323 |
| seed_p_vs_seed_pars | 577 | -0.0826 | -0.1303 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
