# YDL166C
Status: ok. Length: 685 nt. Measured usable bases: 372. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 372 | 0.3815 | 0.3571 |
| rnafold | ok | 372 | 0.2899 | 0.2796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | -0.1539 | -0.0365 |
| seed_p | 85 | -0.1680 | -0.1543 |
| seed_p_vs_seed_pars | 60 | -0.0480 | 0.1857 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
