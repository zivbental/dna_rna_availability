# YJR006W
Status: ok. Length: 1527 nt. Measured usable bases: 559. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 559 | 0.2363 | 0.2304 |
| rnafold | ok | 559 | 0.2527 | 0.2503 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.3157 | -0.5969 |
| seed_p | 51 | -0.4992 | -0.4757 |
| seed_p_vs_seed_pars | 42 | -0.7782 | -0.9015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
