# YCR090C
Status: ok. Length: 624 nt. Measured usable bases: 405. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 405 | 0.2924 | 0.2343 |
| rnafold | ok | 405 | 0.2597 | 0.2300 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 189 | 0.2934 | 0.3546 |
| seed_p | 189 | -0.1379 | 0.0470 |
| seed_p_vs_seed_pars | 130 | 0.0306 | 0.1325 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
