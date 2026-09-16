# YPL244C
Status: ok. Length: 1181 nt. Measured usable bases: 670. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 670 | 0.3402 | 0.3196 |
| rnafold | ok | 670 | 0.2549 | 0.2555 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 271 | -0.0172 | -0.1264 |
| seed_p | 271 | 0.0113 | -0.0943 |
| seed_p_vs_seed_pars | 217 | -0.3435 | -0.3521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
