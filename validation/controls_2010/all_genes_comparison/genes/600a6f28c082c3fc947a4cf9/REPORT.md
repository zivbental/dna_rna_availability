# YPL087W
Status: ok. Length: 1185 nt. Measured usable bases: 628. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 628 | 0.3537 | 0.3504 |
| rnafold | ok | 628 | 0.3386 | 0.3346 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.1206 | -0.3483 |
| seed_p | 137 | -0.1972 | -0.5228 |
| seed_p_vs_seed_pars | 107 | -0.4395 | -0.5125 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
