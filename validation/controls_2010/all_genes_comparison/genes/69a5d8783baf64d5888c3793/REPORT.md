# YGR235C
Status: ok. Length: 838 nt. Measured usable bases: 447. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 447 | 0.3469 | 0.3534 |
| rnafold | ok | 447 | 0.2297 | 0.2221 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | -0.2084 | -0.2691 |
| seed_p | 172 | -0.2103 | -0.2097 |
| seed_p_vs_seed_pars | 126 | -0.3163 | -0.2544 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
