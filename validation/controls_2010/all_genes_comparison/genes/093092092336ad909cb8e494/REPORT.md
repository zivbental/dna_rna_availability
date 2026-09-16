# YPL127C
Status: ok. Length: 1123 nt. Measured usable bases: 598. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 598 | 0.3455 | 0.3553 |
| rnafold | ok | 598 | 0.2871 | 0.3077 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 370 | 0.1216 | 0.0072 |
| seed_p | 370 | -0.1002 | -0.0665 |
| seed_p_vs_seed_pars | 299 | -0.0393 | -0.0007 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
