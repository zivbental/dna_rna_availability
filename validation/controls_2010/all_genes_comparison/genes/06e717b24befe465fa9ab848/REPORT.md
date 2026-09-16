# YFL048C
Status: ok. Length: 1448 nt. Measured usable bases: 977. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 977 | 0.3296 | 0.3176 |
| rnafold | ok | 977 | 0.2933 | 0.2796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 450 | -0.0914 | -0.1011 |
| seed_p | 450 | 0.0190 | -0.0242 |
| seed_p_vs_seed_pars | 379 | -0.0336 | -0.1260 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
