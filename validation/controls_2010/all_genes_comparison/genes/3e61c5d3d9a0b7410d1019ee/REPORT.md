# YBR103W
Status: ok. Length: 1608 nt. Measured usable bases: 662. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 662 | 0.3851 | 0.3769 |
| rnafold | ok | 662 | 0.3210 | 0.3121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.1712 | 0.2023 |
| seed_p | 101 | -0.2014 | -0.2017 |
| seed_p_vs_seed_pars | 58 | -0.2042 | -0.0122 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
