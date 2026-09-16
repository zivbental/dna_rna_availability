# YLL048C
Status: ok. Length: 5243 nt. Measured usable bases: 2957. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2957 | 0.2283 | 0.2235 |
| rnafold | ok | 2957 | 0.1671 | 0.1663 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1040 | 0.1042 | 0.0633 |
| seed_p | 1040 | -0.0535 | 0.0064 |
| seed_p_vs_seed_pars | 818 | -0.3909 | -0.2911 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
