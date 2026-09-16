# YIR016W
Status: ok. Length: 925 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.3352 | 0.3080 |
| rnafold | ok | 454 | 0.2802 | 0.2804 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.1312 | 0.0527 |
| seed_p | 98 | -0.0310 | 0.0781 |
| seed_p_vs_seed_pars | 57 | -0.4479 | -0.2476 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
