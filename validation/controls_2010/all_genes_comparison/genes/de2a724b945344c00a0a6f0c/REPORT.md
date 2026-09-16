# YJR123W
Status: ok. Length: 844 nt. Measured usable bases: 759. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 759 | 0.3093 | 0.2859 |
| rnafold | ok | 759 | 0.2704 | 0.2481 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 751 | -0.1509 | -0.3288 |
| seed_p | 751 | -0.2080 | -0.2381 |
| seed_p_vs_seed_pars | 710 | -0.3235 | -0.3069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
