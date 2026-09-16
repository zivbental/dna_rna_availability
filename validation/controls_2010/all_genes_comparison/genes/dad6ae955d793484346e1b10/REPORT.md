# YNL240C
Status: ok. Length: 1743 nt. Measured usable bases: 908. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 908 | 0.3830 | 0.3710 |
| rnafold | ok | 908 | 0.3117 | 0.3122 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 273 | -0.3412 | -0.3859 |
| seed_p | 273 | -0.2765 | -0.3341 |
| seed_p_vs_seed_pars | 213 | -0.4211 | -0.4712 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
