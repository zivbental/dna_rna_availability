# YNL244C
Status: ok. Length: 473 nt. Measured usable bases: 423. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 423 | 0.3271 | 0.3271 |
| rnafold | ok | 423 | 0.2764 | 0.2879 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 406 | 0.1679 | -0.0728 |
| seed_p | 406 | -0.1129 | -0.0160 |
| seed_p_vs_seed_pars | 381 | -0.2620 | -0.1166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
