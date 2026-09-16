# YGR090W
Status: ok. Length: 3946 nt. Measured usable bases: 1928. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1928 | 0.2801 | 0.2616 |
| rnafold | ok | 1928 | 0.2276 | 0.2202 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 373 | -0.0170 | -0.1108 |
| seed_p | 373 | -0.3177 | -0.2795 |
| seed_p_vs_seed_pars | 298 | -0.5070 | -0.5053 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
