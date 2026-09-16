# YNL008C
Status: ok. Length: 2010 nt. Measured usable bases: 691. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 691 | 0.2308 | 0.2239 |
| rnafold | ok | 691 | 0.1922 | 0.2013 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 38 | -0.0565 | 0.4392 |
| seed_p | 38 | 0.0688 | -0.2726 |
| seed_p_vs_seed_pars | 34 | 0.0682 | -0.3229 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
