# YGR111W
Status: ok. Length: 1353 nt. Measured usable bases: 611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 611 | 0.3562 | 0.3460 |
| rnafold | ok | 611 | 0.3070 | 0.2965 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.0896 | -0.2590 |
| seed_p | 61 | 0.4172 | 0.4064 |
| seed_p_vs_seed_pars | 46 | 0.2698 | 0.3415 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
