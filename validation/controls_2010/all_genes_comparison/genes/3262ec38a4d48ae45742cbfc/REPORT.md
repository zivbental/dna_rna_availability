# YDR387C
Status: ok. Length: 1937 nt. Measured usable bases: 849. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 849 | 0.2017 | 0.1821 |
| rnafold | ok | 849 | 0.1605 | 0.1658 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.0839 | -0.1057 |
| seed_p | 96 | -0.0487 | 0.0664 |
| seed_p_vs_seed_pars | 76 | -0.3436 | -0.0976 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
