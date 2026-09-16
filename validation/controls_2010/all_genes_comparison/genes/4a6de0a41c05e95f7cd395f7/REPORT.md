# YLR342W
Status: ok. Length: 6138 nt. Measured usable bases: 4844. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 4844 | 0.2869 | 0.2668 |
| rnafold | ok | 4844 | 0.2229 | 0.2094 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 3867 | 0.0559 | -0.0380 |
| seed_p | 3867 | -0.0059 | -0.0333 |
| seed_p_vs_seed_pars | 3077 | -0.0814 | -0.0934 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
