# YGL038C
Status: ok. Length: 1661 nt. Measured usable bases: 846. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 846 | 0.2880 | 0.2820 |
| rnafold | ok | 846 | 0.1896 | 0.1983 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.1968 | -0.1598 |
| seed_p | 203 | -0.1300 | -0.0879 |
| seed_p_vs_seed_pars | 95 | -0.0599 | -0.0504 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
