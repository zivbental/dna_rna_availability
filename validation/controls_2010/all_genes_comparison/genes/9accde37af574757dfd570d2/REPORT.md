# YNL290W
Status: ok. Length: 1336 nt. Measured usable bases: 625. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 625 | 0.3717 | 0.3689 |
| rnafold | ok | 625 | 0.3868 | 0.3845 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.0110 | -0.2049 |
| seed_p | 257 | 0.0521 | 0.0512 |
| seed_p_vs_seed_pars | 205 | -0.3049 | -0.2537 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
