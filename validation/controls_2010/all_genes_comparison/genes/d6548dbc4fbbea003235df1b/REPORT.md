# YIL152W
Status: ok. Length: 708 nt. Measured usable bases: 284. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 284 | 0.3554 | 0.3530 |
| rnafold | ok | 284 | 0.4147 | 0.4129 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | -0.3365 | -0.5463 |
| seed_p | 42 | -0.2057 | -0.0833 |
| seed_p_vs_seed_pars | 38 | -0.1414 | 0.1670 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
