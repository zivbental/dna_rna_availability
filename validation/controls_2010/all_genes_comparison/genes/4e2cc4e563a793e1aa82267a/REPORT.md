# YGL050W
Status: ok. Length: 822 nt. Measured usable bases: 351. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 351 | 0.4086 | 0.4128 |
| rnafold | ok | 351 | 0.3509 | 0.3576 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | -0.3776 | -0.2478 |
| seed_p | 26 | -0.2772 | -0.2538 |
| seed_p_vs_seed_pars | 15 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
