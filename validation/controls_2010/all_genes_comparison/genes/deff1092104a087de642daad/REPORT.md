# YDR046C
Status: ok. Length: 1955 nt. Measured usable bases: 1411. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1411 | 0.3130 | 0.2823 |
| rnafold | ok | 1411 | 0.2441 | 0.1948 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 932 | -0.0024 | 0.0049 |
| seed_p | 932 | -0.2278 | -0.1542 |
| seed_p_vs_seed_pars | 727 | -0.4134 | -0.2687 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
