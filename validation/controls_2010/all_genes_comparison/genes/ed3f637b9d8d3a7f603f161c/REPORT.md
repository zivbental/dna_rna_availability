# YGL101W
Status: ok. Length: 1003 nt. Measured usable bases: 516. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 516 | 0.3852 | 0.3887 |
| rnafold | ok | 516 | 0.3694 | 0.3801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 115 | 0.1985 | -0.1680 |
| seed_p | 115 | -0.0131 | -0.1492 |
| seed_p_vs_seed_pars | 72 | 0.2129 | 0.0238 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
