# YER145C
Status: ok. Length: 1327 nt. Measured usable bases: 1036. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1036 | 0.3202 | 0.3108 |
| rnafold | ok | 1036 | 0.2283 | 0.2177 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 828 | 0.0386 | -0.1000 |
| seed_p | 828 | -0.0535 | -0.1108 |
| seed_p_vs_seed_pars | 628 | -0.1862 | -0.2005 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
