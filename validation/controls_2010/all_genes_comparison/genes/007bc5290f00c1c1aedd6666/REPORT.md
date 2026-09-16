# YML057W
Status: ok. Length: 1927 nt. Measured usable bases: 1112. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1112 | 0.3159 | 0.3069 |
| rnafold | ok | 1112 | 0.3088 | 0.2980 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | 0.0545 | -0.0519 |
| seed_p | 377 | -0.4322 | -0.2540 |
| seed_p_vs_seed_pars | 321 | -0.4643 | -0.2037 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
