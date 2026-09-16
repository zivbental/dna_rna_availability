# YIL010W
Status: ok. Length: 856 nt. Measured usable bases: 272. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 272 | 0.3677 | 0.3550 |
| rnafold | ok | 272 | 0.3313 | 0.3194 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | -0.3262 | -0.0397 |
| seed_p | 37 | -0.2781 | -0.4573 |
| seed_p_vs_seed_pars | 34 | -0.0549 | -0.0148 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
