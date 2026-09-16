# YHR146W
Status: ok. Length: 1472 nt. Measured usable bases: 608. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 608 | 0.3730 | 0.3569 |
| rnafold | ok | 608 | 0.2954 | 0.2844 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.4532 | -0.6603 |
| seed_p | 84 | -0.6060 | -0.6246 |
| seed_p_vs_seed_pars | 53 | -0.4782 | -0.5165 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
