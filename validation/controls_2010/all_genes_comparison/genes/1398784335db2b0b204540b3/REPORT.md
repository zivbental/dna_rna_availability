# YKL172W
Status: ok. Length: 1400 nt. Measured usable bases: 541. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 541 | 0.3338 | 0.3295 |
| rnafold | ok | 541 | 0.2959 | 0.2747 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | 0.3352 | 0.3302 |
| seed_p | 50 | 0.2601 | 0.2963 |
| seed_p_vs_seed_pars | 36 | 0.4830 | 0.0625 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
