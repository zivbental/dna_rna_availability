# YIL140W
Status: ok. Length: 2472 nt. Measured usable bases: 1341. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1341 | 0.2430 | 0.2452 |
| rnafold | ok | 1341 | 0.2141 | 0.2394 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | 0.1513 | 0.0782 |
| seed_p | 247 | 0.0206 | 0.0408 |
| seed_p_vs_seed_pars | 163 | -0.2788 | -0.3514 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
