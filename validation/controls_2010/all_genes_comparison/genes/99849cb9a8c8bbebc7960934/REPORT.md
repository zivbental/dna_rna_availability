# YOR039W
Status: ok. Length: 1131 nt. Measured usable bases: 635. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 635 | 0.3445 | 0.3356 |
| rnafold | ok | 635 | 0.2563 | 0.2683 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 304 | -0.2533 | -0.2454 |
| seed_p | 304 | -0.3736 | -0.4323 |
| seed_p_vs_seed_pars | 238 | -0.4101 | -0.4716 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
