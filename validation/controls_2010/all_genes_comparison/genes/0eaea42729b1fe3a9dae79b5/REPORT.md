# YDR151C
Status: ok. Length: 1113 nt. Measured usable bases: 531. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 531 | 0.2933 | 0.2856 |
| rnafold | ok | 531 | 0.2368 | 0.2317 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.4888 | -0.3495 |
| seed_p | 81 | -0.4437 | -0.3712 |
| seed_p_vs_seed_pars | 52 | -0.4228 | -0.2896 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
