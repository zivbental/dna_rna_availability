# YLR387C
Status: ok. Length: 1421 nt. Measured usable bases: 740. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 740 | 0.2684 | 0.2791 |
| rnafold | ok | 740 | 0.2558 | 0.2464 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | -0.3098 | -0.4973 |
| seed_p | 208 | -0.4801 | -0.4335 |
| seed_p_vs_seed_pars | 151 | -0.4475 | -0.4286 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
