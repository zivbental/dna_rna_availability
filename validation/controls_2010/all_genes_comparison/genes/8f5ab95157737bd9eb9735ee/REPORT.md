# YHR070W
Status: ok. Length: 2079 nt. Measured usable bases: 1202. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1202 | 0.2734 | 0.2556 |
| rnafold | ok | 1202 | 0.2059 | 0.2065 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 534 | 0.2874 | -0.1083 |
| seed_p | 534 | -0.1597 | -0.1951 |
| seed_p_vs_seed_pars | 410 | -0.3558 | -0.4127 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
