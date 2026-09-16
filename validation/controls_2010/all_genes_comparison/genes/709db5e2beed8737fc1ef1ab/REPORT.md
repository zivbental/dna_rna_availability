# YGR027C
Status: ok. Length: 738 nt. Measured usable bases: 355. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 355 | 0.3059 | 0.2947 |
| rnafold | ok | 355 | 0.3203 | 0.3285 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.3244 | -0.1439 |
| seed_p | 179 | -0.3257 | -0.2518 |
| seed_p_vs_seed_pars | 131 | -0.6260 | -0.5735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
