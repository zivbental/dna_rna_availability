# YFR034C
Status: ok. Length: 1317 nt. Measured usable bases: 639. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 639 | 0.3140 | 0.2987 |
| rnafold | ok | 639 | 0.2575 | 0.2481 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | 0.0550 | 0.1789 |
| seed_p | 166 | -0.3403 | -0.1646 |
| seed_p_vs_seed_pars | 127 | -0.5759 | -0.4947 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
