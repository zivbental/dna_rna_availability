# YNL288W
Status: ok. Length: 1402 nt. Measured usable bases: 852. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 852 | 0.2418 | 0.2243 |
| rnafold | ok | 852 | 0.2829 | 0.2700 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 421 | -0.0738 | 0.0381 |
| seed_p | 421 | -0.0264 | 0.0041 |
| seed_p_vs_seed_pars | 349 | -0.1768 | -0.1833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
