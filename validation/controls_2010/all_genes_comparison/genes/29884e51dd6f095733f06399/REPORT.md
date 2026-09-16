# YFL004W
Status: ok. Length: 2707 nt. Measured usable bases: 1710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1710 | 0.3333 | 0.3274 |
| rnafold | ok | 1710 | 0.2843 | 0.2765 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 717 | -0.0485 | -0.1176 |
| seed_p | 717 | -0.0654 | -0.0290 |
| seed_p_vs_seed_pars | 556 | -0.2906 | -0.2140 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
