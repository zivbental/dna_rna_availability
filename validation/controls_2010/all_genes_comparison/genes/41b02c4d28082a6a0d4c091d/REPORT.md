# YER165W
Status: ok. Length: 2019 nt. Measured usable bases: 1628. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1628 | 0.3621 | 0.3535 |
| rnafold | ok | 1628 | 0.3016 | 0.2965 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1417 | -0.2122 | -0.0867 |
| seed_p | 1417 | -0.0807 | -0.0143 |
| seed_p_vs_seed_pars | 1234 | -0.1737 | -0.1561 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
