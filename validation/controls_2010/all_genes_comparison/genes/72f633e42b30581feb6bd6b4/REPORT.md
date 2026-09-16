# YJR002W
Status: ok. Length: 2160 nt. Measured usable bases: 1062. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1062 | 0.3780 | 0.3729 |
| rnafold | ok | 1062 | 0.2513 | 0.2507 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 248 | -0.3870 | -0.1367 |
| seed_p | 248 | -0.4523 | -0.4049 |
| seed_p_vs_seed_pars | 164 | -0.5991 | -0.4519 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
