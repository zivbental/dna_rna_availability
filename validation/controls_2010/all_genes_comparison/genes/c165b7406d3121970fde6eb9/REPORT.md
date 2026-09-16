# YFR009W
Status: ok. Length: 2391 nt. Measured usable bases: 1579. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1579 | 0.3274 | 0.3134 |
| rnafold | ok | 1579 | 0.2447 | 0.2403 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 780 | -0.0921 | -0.1401 |
| seed_p | 780 | -0.2191 | -0.2377 |
| seed_p_vs_seed_pars | 551 | -0.3233 | -0.1998 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
