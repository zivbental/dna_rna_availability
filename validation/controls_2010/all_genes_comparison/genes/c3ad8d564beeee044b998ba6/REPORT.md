# YGL194C-A
Status: ok. Length: 447 nt. Measured usable bases: 229. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 229 | 0.4229 | 0.4379 |
| rnafold | ok | 229 | 0.3662 | 0.3608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | -0.2449 | -0.5465 |
| seed_p | 97 | -0.7345 | -0.7203 |
| seed_p_vs_seed_pars | 82 | -0.6279 | -0.5879 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
