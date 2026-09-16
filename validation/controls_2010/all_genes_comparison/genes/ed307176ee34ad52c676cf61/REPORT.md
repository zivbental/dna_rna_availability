# YMR058W
Status: ok. Length: 2101 nt. Measured usable bases: 1811. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1811 | 0.3358 | 0.3185 |
| rnafold | ok | 1811 | 0.2715 | 0.2498 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1660 | -0.0339 | -0.0380 |
| seed_p | 1660 | -0.0942 | -0.1422 |
| seed_p_vs_seed_pars | 1431 | -0.2961 | -0.3373 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
